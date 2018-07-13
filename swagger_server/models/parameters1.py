# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Parameters1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, status: str=None, message: str=None, sim_time: int=None, plan: List[str]=None, config: List[str]=None, sensors: List[str]=None):  # noqa: E501
        """Parameters1 - a model defined in Swagger

        :param status: The status of this Parameters1.  # noqa: E501
        :type status: str
        :param message: The message of this Parameters1.  # noqa: E501
        :type message: str
        :param sim_time: The sim_time of this Parameters1.  # noqa: E501
        :type sim_time: int
        :param plan: The plan of this Parameters1.  # noqa: E501
        :type plan: List[str]
        :param config: The config of this Parameters1.  # noqa: E501
        :type config: List[str]
        :param sensors: The sensors of this Parameters1.  # noqa: E501
        :type sensors: List[str]
        """
        self.swagger_types = {
            'status': str,
            'message': str,
            'sim_time': int,
            'plan': List[str],
            'config': List[str],
            'sensors': List[str]
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message',
            'sim_time': 'sim-time',
            'plan': 'plan',
            'config': 'config',
            'sensors': 'sensors'
        }

        self._status = status
        self._message = message
        self._sim_time = sim_time
        self._plan = plan
        self._config = config
        self._sensors = sensors

    @classmethod
    def from_dict(cls, dikt) -> 'Parameters1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameters_1 of this Parameters1.  # noqa: E501
        :rtype: Parameters1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> str:
        """Gets the status of this Parameters1.

        one of a enumerated set of statuses to report, arise, as follows:   * `live`, the SUT has processed the configuration data      and is ready for initial perturbations (if any) and the      start of the test   * `mission-running`, the SUT has processed the initial      perturbations after receiving `/start`, possibly      adapted, and the robot is now actually moving along      its path. it is an error to send any perturbation to      the SUT between sending a message to `/start` and      receiving this status.   * `adapting`, the SUT has detected a condition that      requires adaptation and the SUT is adapting. it is      an error to send any perturbation to the SUT after      this message is sent to the TH until the TH gets a      status message with `adapted`.   * `adapted`, the SUT has finished adapting after      observing a need to. this means that the robot is      moving along its plan again and it is no longer an      error to send perturbations. if this is the status      code of the message, the fields `plan`, `config` and      `sensors` will also be present, to describe the new      state of the robot.  # noqa: E501

        :return: The status of this Parameters1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Parameters1.

        one of a enumerated set of statuses to report, arise, as follows:   * `live`, the SUT has processed the configuration data      and is ready for initial perturbations (if any) and the      start of the test   * `mission-running`, the SUT has processed the initial      perturbations after receiving `/start`, possibly      adapted, and the robot is now actually moving along      its path. it is an error to send any perturbation to      the SUT between sending a message to `/start` and      receiving this status.   * `adapting`, the SUT has detected a condition that      requires adaptation and the SUT is adapting. it is      an error to send any perturbation to the SUT after      this message is sent to the TH until the TH gets a      status message with `adapted`.   * `adapted`, the SUT has finished adapting after      observing a need to. this means that the robot is      moving along its plan again and it is no longer an      error to send perturbations. if this is the status      code of the message, the fields `plan`, `config` and      `sensors` will also be present, to describe the new      state of the robot.  # noqa: E501

        :param status: The status of this Parameters1.
        :type status: str
        """
        allowed_values = ["live", "mission-running", "adapting", "adapted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self) -> str:
        """Gets the message of this Parameters1.

        human readable text describing the status, if any  # noqa: E501

        :return: The message of this Parameters1.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Parameters1.

        human readable text describing the status, if any  # noqa: E501

        :param message: The message of this Parameters1.
        :type message: str
        """

        self._message = message

    @property
    def sim_time(self) -> int:
        """Gets the sim_time of this Parameters1.

        the simulation time the status message was produced  # noqa: E501

        :return: The sim_time of this Parameters1.
        :rtype: int
        """
        return self._sim_time

    @sim_time.setter
    def sim_time(self, sim_time: int):
        """Sets the sim_time of this Parameters1.

        the simulation time the status message was produced  # noqa: E501

        :param sim_time: The sim_time of this Parameters1.
        :type sim_time: int
        """
        if sim_time is None:
            raise ValueError("Invalid value for `sim_time`, must not be `None`")  # noqa: E501
        if sim_time is not None and sim_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `sim_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sim_time = sim_time

    @property
    def plan(self) -> List[str]:
        """Gets the plan of this Parameters1.

        list of waypoints the current plan tends to visit, in order. This will not be sent with `status == live`.  # noqa: E501

        :return: The plan of this Parameters1.
        :rtype: List[str]
        """
        return self._plan

    @plan.setter
    def plan(self, plan: List[str]):
        """Sets the plan of this Parameters1.

        list of waypoints the current plan tends to visit, in order. This will not be sent with `status == live`.  # noqa: E501

        :param plan: The plan of this Parameters1.
        :type plan: List[str]
        """

        self._plan = plan

    @property
    def config(self) -> List[str]:
        """Gets the config of this Parameters1.

        list of currently active nodes. This will not be sent with `status == live`.  # noqa: E501

        :return: The config of this Parameters1.
        :rtype: List[str]
        """
        return self._config

    @config.setter
    def config(self, config: List[str]):
        """Sets the config of this Parameters1.

        list of currently active nodes. This will not be sent with `status == live`.  # noqa: E501

        :param config: The config of this Parameters1.
        :type config: List[str]
        """
        allowed_values = ["amcl-kinect", "amcl-lidar", "mrpt-kinect", "mrpt-lidar", "aruco-camera"]  # noqa: E501
        if not set(config).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `config` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(config) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._config = config

    @property
    def sensors(self) -> List[str]:
        """Gets the sensors of this Parameters1.

        list of currently active sensors, in order. This will not be sent with `status == live`.  # noqa: E501

        :return: The sensors of this Parameters1.
        :rtype: List[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors: List[str]):
        """Sets the sensors of this Parameters1.

        list of currently active sensors, in order. This will not be sent with `status == live`.  # noqa: E501

        :param sensors: The sensors of this Parameters1.
        :type sensors: List[str]
        """
        allowed_values = ["kinect", "lidar", "camera", "headlamp"]  # noqa: E501
        if not set(sensors).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `sensors` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(sensors) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._sensors = sensors
