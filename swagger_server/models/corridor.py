# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Corridor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, start: str=None, end: str=None):  # noqa: E501
        """Corridor - a model defined in Swagger

        :param start: The start of this Corridor.  # noqa: E501
        :type start: str
        :param end: The end of this Corridor.  # noqa: E501
        :type end: str
        """
        self.swagger_types = {
            'start': str,
            'end': str
        }

        self.attribute_map = {
            'start': 'start',
            'end': 'end'
        }

        self._start = start
        self._end = end

    @classmethod
    def from_dict(cls, dikt) -> 'Corridor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Corridor of this Corridor.  # noqa: E501
        :rtype: Corridor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self) -> str:
        """Gets the start of this Corridor.


        :return: The start of this Corridor.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start: str):
        """Sets the start of this Corridor.


        :param start: The start of this Corridor.
        :type start: str
        """

        self._start = start

    @property
    def end(self) -> str:
        """Gets the end of this Corridor.


        :return: The end of this Corridor.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end: str):
        """Sets the end of this Corridor.


        :param end: The end of this Corridor.
        :type end: str
        """

        self._end = end
