# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.parameters import Parameters  # noqa: E501
from swagger_server.models.parameters1 import Parameters1  # noqa: E501
from swagger_server.models.parameters2 import Parameters2  # noqa: E501
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

    def test_ready_post(self):
        """Test case for ready_post

        
        """
        response = self.client.open(
            '/ready',
            method='POST')
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
