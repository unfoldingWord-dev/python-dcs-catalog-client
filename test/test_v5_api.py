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
from dcs_catalog_client.api.v5_api import V5Api  # noqa: E501
from dcs_catalog_client.rest import ApiException


class TestV5Api(unittest.TestCase):
    """V5Api unit test stubs"""

    def setUp(self):
        self.api = dcs_catalog_client.api.v5_api.V5Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_v5_get_catalog_entry(self):
        """Test case for v5_get_catalog_entry

        Catalog entry  # noqa: E501
        """
        pass

    def test_v5_get_metadata(self):
        """Test case for v5_get_metadata

        Catalog entry metadata (manifest.yaml in JSON format)  # noqa: E501
        """
        pass

    def test_v5_search(self):
        """Test case for v5_search

        Catalog search  # noqa: E501
        """
        pass

    def test_v5_search_owner(self):
        """Test case for v5_search_owner

        Catalog search by owner  # noqa: E501
        """
        pass

    def test_v5_search_repo(self):
        """Test case for v5_search_repo

        Catalog search by repo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
