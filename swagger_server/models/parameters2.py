# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.collision_data import CollisionData  # noqa: F401,E501
from swagger_server import util


class Parameters2(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, final_x: float=None, final_y: float=None, final_sim_time: int=None, final_charge: int=None, collisions: List[CollisionData]=None, num_adaptations: int=None, final_utility: float=None):  # noqa: E501
        """Parameters2 - a model defined in Swagger

        :param final_x: The final_x of this Parameters2.  # noqa: E501
        :type final_x: float
        :param final_y: The final_y of this Parameters2.  # noqa: E501
        :type final_y: float
        :param final_sim_time: The final_sim_time of this Parameters2.  # noqa: E501
        :type final_sim_time: int
        :param final_charge: The final_charge of this Parameters2.  # noqa: E501
        :type final_charge: int
        :param collisions: The collisions of this Parameters2.  # noqa: E501
        :type collisions: List[CollisionData]
        :param num_adaptations: The num_adaptations of this Parameters2.  # noqa: E501
        :type num_adaptations: int
        :param final_utility: The final_utility of this Parameters2.  # noqa: E501
        :type final_utility: float
        """
        self.swagger_types = {
            'final_x': float,
            'final_y': float,
            'final_sim_time': int,
            'final_charge': int,
            'collisions': List[CollisionData],
            'num_adaptations': int,
            'final_utility': float
        }

        self.attribute_map = {
            'final_x': 'final-x',
            'final_y': 'final-y',
            'final_sim_time': 'final-sim-time',
            'final_charge': 'final-charge',
            'collisions': 'collisions',
            'num_adaptations': 'num-adaptations',
            'final_utility': 'final-utility'
        }

        self._final_x = final_x
        self._final_y = final_y
        self._final_sim_time = final_sim_time
        self._final_charge = final_charge
        self._collisions = collisions
        self._num_adaptations = num_adaptations
        self._final_utility = final_utility

    @classmethod
    def from_dict(cls, dikt) -> 'Parameters2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameters_2 of this Parameters2.  # noqa: E501
        :rtype: Parameters2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def final_x(self) -> float:
        """Gets the final_x of this Parameters2.

        the x coordinate of the robot position when the test ended  # noqa: E501

        :return: The final_x of this Parameters2.
        :rtype: float
        """
        return self._final_x

    @final_x.setter
    def final_x(self, final_x: float):
        """Sets the final_x of this Parameters2.

        the x coordinate of the robot position when the test ended  # noqa: E501

        :param final_x: The final_x of this Parameters2.
        :type final_x: float
        """
        if final_x is None:
            raise ValueError("Invalid value for `final_x`, must not be `None`")  # noqa: E501

        self._final_x = final_x

    @property
    def final_y(self) -> float:
        """Gets the final_y of this Parameters2.

        the y coordinate of the robot position when the test ended  # noqa: E501

        :return: The final_y of this Parameters2.
        :rtype: float
        """
        return self._final_y

    @final_y.setter
    def final_y(self, final_y: float):
        """Sets the final_y of this Parameters2.

        the y coordinate of the robot position when the test ended  # noqa: E501

        :param final_y: The final_y of this Parameters2.
        :type final_y: float
        """
        if final_y is None:
            raise ValueError("Invalid value for `final_y`, must not be `None`")  # noqa: E501

        self._final_y = final_y

    @property
    def final_sim_time(self) -> int:
        """Gets the final_sim_time of this Parameters2.

        the simulation time when the mission finished  # noqa: E501

        :return: The final_sim_time of this Parameters2.
        :rtype: int
        """
        return self._final_sim_time

    @final_sim_time.setter
    def final_sim_time(self, final_sim_time: int):
        """Sets the final_sim_time of this Parameters2.

        the simulation time when the mission finished  # noqa: E501

        :param final_sim_time: The final_sim_time of this Parameters2.
        :type final_sim_time: int
        """
        if final_sim_time is None:
            raise ValueError("Invalid value for `final_sim_time`, must not be `None`")  # noqa: E501
        if final_sim_time is not None and final_sim_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `final_sim_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._final_sim_time = final_sim_time

    @property
    def final_charge(self) -> int:
        """Gets the final_charge of this Parameters2.

        the charge left in the battery when the test ended  # noqa: E501

        :return: The final_charge of this Parameters2.
        :rtype: int
        """
        return self._final_charge

    @final_charge.setter
    def final_charge(self, final_charge: int):
        """Sets the final_charge of this Parameters2.

        the charge left in the battery when the test ended  # noqa: E501

        :param final_charge: The final_charge of this Parameters2.
        :type final_charge: int
        """
        if final_charge is None:
            raise ValueError("Invalid value for `final_charge`, must not be `None`")  # noqa: E501
        if final_charge is not None and final_charge < 0:  # noqa: E501
            raise ValueError("Invalid value for `final_charge`, must be a value greater than or equal to `0`")  # noqa: E501

        self._final_charge = final_charge

    @property
    def collisions(self) -> List[CollisionData]:
        """Gets the collisions of this Parameters2.

        A (possibly empty) list of locations, times, and speeds of any collisions of the robot  # noqa: E501

        :return: The collisions of this Parameters2.
        :rtype: List[CollisionData]
        """
        return self._collisions

    @collisions.setter
    def collisions(self, collisions: List[CollisionData]):
        """Sets the collisions of this Parameters2.

        A (possibly empty) list of locations, times, and speeds of any collisions of the robot  # noqa: E501

        :param collisions: The collisions of this Parameters2.
        :type collisions: List[CollisionData]
        """
        if collisions is None:
            raise ValueError("Invalid value for `collisions`, must not be `None`")  # noqa: E501

        self._collisions = collisions

    @property
    def num_adaptations(self) -> int:
        """Gets the num_adaptations of this Parameters2.

        the number of times that the robot adapted (0 if there is no DAS)  # noqa: E501

        :return: The num_adaptations of this Parameters2.
        :rtype: int
        """
        return self._num_adaptations

    @num_adaptations.setter
    def num_adaptations(self, num_adaptations: int):
        """Sets the num_adaptations of this Parameters2.

        the number of times that the robot adapted (0 if there is no DAS)  # noqa: E501

        :param num_adaptations: The num_adaptations of this Parameters2.
        :type num_adaptations: int
        """
        if num_adaptations is None:
            raise ValueError("Invalid value for `num_adaptations`, must not be `None`")  # noqa: E501
        if num_adaptations is not None and num_adaptations < 0:  # noqa: E501
            raise ValueError("Invalid value for `num_adaptations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_adaptations = num_adaptations

    @property
    def final_utility(self) -> float:
        """Gets the final_utility of this Parameters2.

        the utility achieved at the end of the mission, in the range [0,1]  # noqa: E501

        :return: The final_utility of this Parameters2.
        :rtype: float
        """
        return self._final_utility

    @final_utility.setter
    def final_utility(self, final_utility: float):
        """Sets the final_utility of this Parameters2.

        the utility achieved at the end of the mission, in the range [0,1]  # noqa: E501

        :param final_utility: The final_utility of this Parameters2.
        :type final_utility: float
        """
        if final_utility is None:
            raise ValueError("Invalid value for `final_utility`, must not be `None`")  # noqa: E501
        if final_utility is not None and final_utility > 1:  # noqa: E501
            raise ValueError("Invalid value for `final_utility`, must be a value less than or equal to `1`")  # noqa: E501
        if final_utility is not None and final_utility < 0:  # noqa: E501
            raise ValueError("Invalid value for `final_utility`, must be a value greater than or equal to `0`")  # noqa: E501

        self._final_utility = final_utility