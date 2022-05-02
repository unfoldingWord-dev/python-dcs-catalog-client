# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 1.16.7+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dcs_catalog_client
from dcs_catalog_client.api.v4_api import V4Api  # noqa: E501
from dcs_catalog_client.rest import ApiException


class TestV4Api(unittest.TestCase):
    """V4Api unit test stubs"""

    def setUp(self):
        self.api = dcs_catalog_client.api.v4_api.V4Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_catalo4_search_owner(self):
        """Test case for catalo4_search_owner

        Catalog search by owner  # noqa: E501
        """
        pass

    def test_catalog_get_entry(self):
        """Test case for catalog_get_entry

        Catalog entry  # noqa: E501
        """
        pass

    def test_catalog_get_metadata(self):
        """Test case for catalog_get_metadata

        Catalog entry metadata (manifest.yaml in JSON format)  # noqa: E501
        """
        pass

    def test_catalog_search(self):
        """Test case for catalog_search

        Catalog search  # noqa: E501
        """
        pass

    def test_catalog_search_repo(self):
        """Test case for catalog_search_repo

        Catalog search by repo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
