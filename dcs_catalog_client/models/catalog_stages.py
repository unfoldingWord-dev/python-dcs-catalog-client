# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 1.16.8+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_catalog_client.configuration import Configuration


class CatalogStages(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'draft': 'CatalogStage',
        'latest': 'CatalogStage',
        'preprod': 'CatalogStage',
        'prod': 'CatalogStage'
    }

    attribute_map = {
        'draft': 'draft',
        'latest': 'latest',
        'preprod': 'preprod',
        'prod': 'prod'
    }

    def __init__(self, draft=None, latest=None, preprod=None, prod=None, _configuration=None):  # noqa: E501
        """CatalogStages - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._draft = None
        self._latest = None
        self._preprod = None
        self._prod = None
        self.discriminator = None

        if draft is not None:
            self.draft = draft
        if latest is not None:
            self.latest = latest
        if preprod is not None:
            self.preprod = preprod
        if prod is not None:
            self.prod = prod

    @property
    def draft(self):
        """Gets the draft of this CatalogStages.  # noqa: E501


        :return: The draft of this CatalogStages.  # noqa: E501
        :rtype: CatalogStage
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this CatalogStages.


        :param draft: The draft of this CatalogStages.  # noqa: E501
        :type: CatalogStage
        """

        self._draft = draft

    @property
    def latest(self):
        """Gets the latest of this CatalogStages.  # noqa: E501


        :return: The latest of this CatalogStages.  # noqa: E501
        :rtype: CatalogStage
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this CatalogStages.


        :param latest: The latest of this CatalogStages.  # noqa: E501
        :type: CatalogStage
        """

        self._latest = latest

    @property
    def preprod(self):
        """Gets the preprod of this CatalogStages.  # noqa: E501


        :return: The preprod of this CatalogStages.  # noqa: E501
        :rtype: CatalogStage
        """
        return self._preprod

    @preprod.setter
    def preprod(self, preprod):
        """Sets the preprod of this CatalogStages.


        :param preprod: The preprod of this CatalogStages.  # noqa: E501
        :type: CatalogStage
        """

        self._preprod = preprod

    @property
    def prod(self):
        """Gets the prod of this CatalogStages.  # noqa: E501


        :return: The prod of this CatalogStages.  # noqa: E501
        :rtype: CatalogStage
        """
        return self._prod

    @prod.setter
    def prod(self, prod):
        """Sets the prod of this CatalogStages.


        :param prod: The prod of this CatalogStages.  # noqa: E501
        :type: CatalogStage
        """

        self._prod = prod

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CatalogStages, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CatalogStages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogStages):
            return True

        return self.to_dict() != other.to_dict()
