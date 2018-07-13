# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.parameters import Parameters  # noqa: E501
from swagger_server.models.parameters1 import Parameters1  # noqa: E501
from swagger_server.models.parameters2 import Parameters2  # noqa: E501
from swagger_server.models.start_configuration import StartConfiguration  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_done_post(self):
        """Test case for done_post

        
        """
        Parameters = Parameters2()
        response = self.client.open(
            '/done',
            method='POST',
            data=json.dumps(Parameters),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_error_post(self):
        """Test case for error_post

        
        """
        Parameters = Parameters()
        response = self.client.open(
            '/error',
            method='POST',
            data=json.dumps(Parameters),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_info_get(self):
        """Test case for info_get

        
        """
        response = self.client.open(
            '/info',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ready_post(self):
        """Test case for ready_post

        
        """
        response = self.client.open(
            '/ready',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_post(self):
        """Test case for start_post

        
        """
        StartConfiguration = StartConfiguration()
        response = self.client.open(
            '/start',
            method='POST',
            data=json.dumps(StartConfiguration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_status_post(self):
        """Test case for status_post

        
        """
        Parameters = Parameters1()
        response = self.client.open(
            '/status',
            method='POST',
            data=json.dumps(Parameters),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
