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
from esp_sdk.apis.metadata_api import MetadataApi


class TestMetadataApi(unittest.TestCase):
    """ MetadataApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.metadata_api.MetadataApi()

    def tearDown(self):
        pass

    def test_for_alert(self):
        """
        Test case for for_alert

        Show the metadata for an alert
        """
        pass

    def test_show(self):
        """
        Test case for show

        Show a single Metadata
        """
        pass


if __name__ == '__main__':
    unittest.main()
