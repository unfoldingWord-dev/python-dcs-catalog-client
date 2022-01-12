# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_catalog_client.configuration import Configuration


class CatalogV3Pivoted(object):
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
        'catalogs': 'list[dict(str, str)]',
        'last_updated': 'datetime',
        'subjects': 'list[CatalogV3Subject]'
    }

    attribute_map = {
        'catalogs': 'catalogs',
        'last_updated': 'last_updated',
        'subjects': 'subjects'
    }

    def __init__(self, catalogs=None, last_updated=None, subjects=None, _configuration=None):  # noqa: E501
        """CatalogV3Pivoted - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._catalogs = None
        self._last_updated = None
        self._subjects = None
        self.discriminator = None

        if catalogs is not None:
            self.catalogs = catalogs
        if last_updated is not None:
            self.last_updated = last_updated
        if subjects is not None:
            self.subjects = subjects

    @property
    def catalogs(self):
        """Gets the catalogs of this CatalogV3Pivoted.  # noqa: E501


        :return: The catalogs of this CatalogV3Pivoted.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._catalogs

    @catalogs.setter
    def catalogs(self, catalogs):
        """Sets the catalogs of this CatalogV3Pivoted.


        :param catalogs: The catalogs of this CatalogV3Pivoted.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._catalogs = catalogs

    @property
    def last_updated(self):
        """Gets the last_updated of this CatalogV3Pivoted.  # noqa: E501


        :return: The last_updated of this CatalogV3Pivoted.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this CatalogV3Pivoted.


        :param last_updated: The last_updated of this CatalogV3Pivoted.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def subjects(self):
        """Gets the subjects of this CatalogV3Pivoted.  # noqa: E501


        :return: The subjects of this CatalogV3Pivoted.  # noqa: E501
        :rtype: list[CatalogV3Subject]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this CatalogV3Pivoted.


        :param subjects: The subjects of this CatalogV3Pivoted.  # noqa: E501
        :type: list[CatalogV3Subject]
        """

        self._subjects = subjects

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
        if issubclass(CatalogV3Pivoted, dict):
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
        if not isinstance(other, CatalogV3Pivoted):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogV3Pivoted):
            return True

        return self.to_dict() != other.to_dict()