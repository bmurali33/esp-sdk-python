# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2_sdk
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.suppressions_api import SuppressionsApi


class TestSuppressionsApi(unittest.TestCase):
    """ SuppressionsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.suppressions_api.SuppressionsApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Create a suppression
        """
        pass

    def test_create_from_alert(self):
        """
        Test case for create_from_alert

        Creates a suppression from an alert
        """
        pass

    def test_deactivate(self):
        """
        Test case for deactivate

        Deactivate a suppression
        """
        pass

    def test_list(self):
        """
        Test case for list

        Get a list of Suppressions
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single Suppression
        """
        pass

    def test_update(self):
        """
        Test case for update

        Update a(n) Suppression
        """
        pass


if __name__ == '__main__':
    unittest.main()
