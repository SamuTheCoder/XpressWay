# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.v1_payments_body import V1PaymentsBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_v1_payments_post(self):
        """Test case for v1_payments_post

        Create a new payment
        """
        body = V1PaymentsBody()
        response = self.client.open(
            '/SamuTheCoder/XpressWay/1.0.0/v1/payments',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
