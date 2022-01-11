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


class CatalogV3Subject(object):
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
        'direction': 'str',
        'identifier': 'str',
        'language': 'str',
        'last_updated': 'datetime',
        'resources': 'list[CatalogV3Resource]',
        'subject': 'str',
        'title': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'identifier': 'identifier',
        'language': 'language',
        'last_updated': 'last_updated',
        'resources': 'resources',
        'subject': 'subject',
        'title': 'title'
    }

    def __init__(self, direction=None, identifier=None, language=None, last_updated=None, resources=None, subject=None, title=None, _configuration=None):  # noqa: E501
        """CatalogV3Subject - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._direction = None
        self._identifier = None
        self._language = None
        self._last_updated = None
        self._resources = None
        self._subject = None
        self._title = None
        self.discriminator = None

        if direction is not None:
            self.direction = direction
        if identifier is not None:
            self.identifier = identifier
        if language is not None:
            self.language = language
        if last_updated is not None:
            self.last_updated = last_updated
        if resources is not None:
            self.resources = resources
        if subject is not None:
            self.subject = subject
        if title is not None:
            self.title = title

    @property
    def direction(self):
        """Gets the direction of this CatalogV3Subject.  # noqa: E501


        :return: The direction of this CatalogV3Subject.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this CatalogV3Subject.


        :param direction: The direction of this CatalogV3Subject.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def identifier(self):
        """Gets the identifier of this CatalogV3Subject.  # noqa: E501


        :return: The identifier of this CatalogV3Subject.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this CatalogV3Subject.


        :param identifier: The identifier of this CatalogV3Subject.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def language(self):
        """Gets the language of this CatalogV3Subject.  # noqa: E501


        :return: The language of this CatalogV3Subject.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CatalogV3Subject.


        :param language: The language of this CatalogV3Subject.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def last_updated(self):
        """Gets the last_updated of this CatalogV3Subject.  # noqa: E501


        :return: The last_updated of this CatalogV3Subject.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this CatalogV3Subject.


        :param last_updated: The last_updated of this CatalogV3Subject.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def resources(self):
        """Gets the resources of this CatalogV3Subject.  # noqa: E501


        :return: The resources of this CatalogV3Subject.  # noqa: E501
        :rtype: list[CatalogV3Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CatalogV3Subject.


        :param resources: The resources of this CatalogV3Subject.  # noqa: E501
        :type: list[CatalogV3Resource]
        """

        self._resources = resources

    @property
    def subject(self):
        """Gets the subject of this CatalogV3Subject.  # noqa: E501


        :return: The subject of this CatalogV3Subject.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CatalogV3Subject.


        :param subject: The subject of this CatalogV3Subject.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def title(self):
        """Gets the title of this CatalogV3Subject.  # noqa: E501


        :return: The title of this CatalogV3Subject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CatalogV3Subject.


        :param title: The title of this CatalogV3Subject.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(CatalogV3Subject, dict):
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
        if not isinstance(other, CatalogV3Subject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogV3Subject):
            return True

        return self.to_dict() != other.to_dict()
