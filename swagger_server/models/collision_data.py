# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CollisionData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, robot_x: float=None, robot_y: float=None, robot_speed: float=None, sim_time: int=None):  # noqa: E501
        """CollisionData - a model defined in Swagger

        :param robot_x: The robot_x of this CollisionData.  # noqa: E501
        :type robot_x: float
        :param robot_y: The robot_y of this CollisionData.  # noqa: E501
        :type robot_y: float
        :param robot_speed: The robot_speed of this CollisionData.  # noqa: E501
        :type robot_speed: float
        :param sim_time: The sim_time of this CollisionData.  # noqa: E501
        :type sim_time: int
        """
        self.swagger_types = {
            'robot_x': float,
            'robot_y': float,
            'robot_speed': float,
            'sim_time': int
        }

        self.attribute_map = {
            'robot_x': 'robot-x',
            'robot_y': 'robot-y',
            'robot_speed': 'robot-speed',
            'sim_time': 'sim-time'
        }

        self._robot_x = robot_x
        self._robot_y = robot_y
        self._robot_speed = robot_speed
        self._sim_time = sim_time

    @classmethod
    def from_dict(cls, dikt) -> 'CollisionData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CollisionData of this CollisionData.  # noqa: E501
        :rtype: CollisionData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def robot_x(self) -> float:
        """Gets the robot_x of this CollisionData.

        The x location of the robot center when collision occured  # noqa: E501

        :return: The robot_x of this CollisionData.
        :rtype: float
        """
        return self._robot_x

    @robot_x.setter
    def robot_x(self, robot_x: float):
        """Sets the robot_x of this CollisionData.

        The x location of the robot center when collision occured  # noqa: E501

        :param robot_x: The robot_x of this CollisionData.
        :type robot_x: float
        """
        if robot_x is None:
            raise ValueError("Invalid value for `robot_x`, must not be `None`")  # noqa: E501

        self._robot_x = robot_x

    @property
    def robot_y(self) -> float:
        """Gets the robot_y of this CollisionData.

        The y lcoation of the robot center when collision occured  # noqa: E501

        :return: The robot_y of this CollisionData.
        :rtype: float
        """
        return self._robot_y

    @robot_y.setter
    def robot_y(self, robot_y: float):
        """Sets the robot_y of this CollisionData.

        The y lcoation of the robot center when collision occured  # noqa: E501

        :param robot_y: The robot_y of this CollisionData.
        :type robot_y: float
        """
        if robot_y is None:
            raise ValueError("Invalid value for `robot_y`, must not be `None`")  # noqa: E501

        self._robot_y = robot_y

    @property
    def robot_speed(self) -> float:
        """Gets the robot_speed of this CollisionData.

        The speed of the robot (m/s) at the time the collision occured  # noqa: E501

        :return: The robot_speed of this CollisionData.
        :rtype: float
        """
        return self._robot_speed

    @robot_speed.setter
    def robot_speed(self, robot_speed: float):
        """Sets the robot_speed of this CollisionData.

        The speed of the robot (m/s) at the time the collision occured  # noqa: E501

        :param robot_speed: The robot_speed of this CollisionData.
        :type robot_speed: float
        """
        if robot_speed is None:
            raise ValueError("Invalid value for `robot_speed`, must not be `None`")  # noqa: E501

        self._robot_speed = robot_speed

    @property
    def sim_time(self) -> int:
        """Gets the sim_time of this CollisionData.

        The (simulation) time at which the collision occurred (seconds from start of simulator)  # noqa: E501

        :return: The sim_time of this CollisionData.
        :rtype: int
        """
        return self._sim_time

    @sim_time.setter
    def sim_time(self, sim_time: int):
        """Sets the sim_time of this CollisionData.

        The (simulation) time at which the collision occurred (seconds from start of simulator)  # noqa: E501

        :param sim_time: The sim_time of this CollisionData.
        :type sim_time: int
        """
        if sim_time is None:
            raise ValueError("Invalid value for `sim_time`, must not be `None`")  # noqa: E501

        self._sim_time = sim_time
