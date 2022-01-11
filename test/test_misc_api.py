# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dcs_catalog_client
from dcs_catalog_client.api.misc_api import MiscApi  # noqa: E501
from dcs_catalog_client.rest import ApiException


class TestMiscApi(unittest.TestCase):
    """MiscApi unit test stubs"""

    def setUp(self):
        self.api = dcs_catalog_client.api.misc_api.MiscApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_misc_list_catalog_version_endpoints(self):
        """Test case for misc_list_catalog_version_endpoints

        Catalog Next version endpoint list, including what version \"latest\" points to  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
