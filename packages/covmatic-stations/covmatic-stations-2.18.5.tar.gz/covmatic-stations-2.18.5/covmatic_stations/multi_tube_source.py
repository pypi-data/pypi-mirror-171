import logging

from .utils import WellWithVolume, MoveWithSpeed


class MultiTubeSource(object):
    """

    """
    def __init__(self, name="", logger=None,
                 vertical_speed: int = None,
                 vertical_slow_start_overheight: int = 10):
        self._source_tubes_and_vol = []
        self._name = name
        self._vertical_speed = vertical_speed
        self._vertical_slow_start_overheight = vertical_slow_start_overheight
        if logger:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)
        self._aspirate_list = []

    def append_tube_with_vol(self, source, available_volume):
        self._source_tubes_and_vol.append(dict(source=source,
                                               available_volume=available_volume))
        self.logger.debug("{}: appended {} with {}ul".format(self._name, source, available_volume))
        self.logger.debug("Now sources is: {}".format(self._source_tubes_and_vol))

    def prepare_aspiration(self, volume, fixed_height: float = None, min_height: float = 0.5):
        """ Prepare the aspiration list for the requested volume
        @parameter volume: the volume in ul to aspirate;
        @parameter fixed_height: if set force the aspiration at this height from bottom;
        @parameter min_height: the minimum height to reach from bottom with automatic height calculation"""
        self._aspirate_list = []
        left_volume = volume
        for source_and_vol in self._source_tubes_and_vol:
            if source_and_vol["available_volume"] >= left_volume:
                # aspirate_list.append(dict(source=source_and_vol["source"], vol=left_volume))
                aspirate_vol = left_volume
            else:
                aspirate_vol = source_and_vol["available_volume"]
            left_volume -= aspirate_vol
            source_and_vol["available_volume"] -= aspirate_vol
            if aspirate_vol != 0:
                if fixed_height is None:
                    height = WellWithVolume(
                        well=source_and_vol["source"],
                        initial_vol=source_and_vol["available_volume"],
                        min_height=min_height).height
                else:
                    height = fixed_height
                self._aspirate_list.append(dict(source=source_and_vol["source"], vol=aspirate_vol, height=height))

            if left_volume == 0:
                break
        else:
            raise Exception("{}: no volume left in source tubes.".format(self._name))

        self.logger.debug("{} sources: {}".format(self._name, self._source_tubes_and_vol))

    def aspirate(self, pip):
        assert self._aspirate_list, "You must call calculate_aspirate_volume before aspirate"
        for a in self._aspirate_list:
            if self._vertical_speed is not None:
                with MoveWithSpeed(pip,
                                   from_point=a["source"].bottom(a["height"] + self._vertical_slow_start_overheight),
                                   to_point=a["source"].bottom(a["height"]),
                                   speed=self._vertical_speed, move_close=False):
                    pip.aspirate(a["vol"])
            else:
                pip.aspirate(a["vol"], a["source"].bottom(a["height"]))

    @property
    def locations_str(self):
        return "{}: ".format(self._name) + \
               " ".join(["{}; ".format(sv['source'])
                         for sv in self._source_tubes_and_vol])

    def __str__(self):
        return "{}: ".format(self._name) +\
               " ".join(["{} with volume {}ul;".format(sv['source'], sv['available_volume'])
                        for sv in self._source_tubes_and_vol])
