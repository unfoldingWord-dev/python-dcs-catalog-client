# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.15.0-rc3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from giteapy.configuration import Configuration


class CreateLabelOption(object):
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
        'color': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'color': 'color',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, color=None, description=None, name=None, _configuration=None):  # noqa: E501
        """CreateLabelOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._color = None
        self._description = None
        self._name = None
        self.discriminator = None

        self.color = color
        if description is not None:
            self.description = description
        self.name = name

    @property
    def color(self):
        """Gets the color of this CreateLabelOption.  # noqa: E501


        :return: The color of this CreateLabelOption.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this CreateLabelOption.


        :param color: The color of this CreateLabelOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def description(self):
        """Gets the description of this CreateLabelOption.  # noqa: E501


        :return: The description of this CreateLabelOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLabelOption.


        :param description: The description of this CreateLabelOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateLabelOption.  # noqa: E501


        :return: The name of this CreateLabelOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLabelOption.


        :param name: The name of this CreateLabelOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(CreateLabelOption, dict):
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
        if not isinstance(other, CreateLabelOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateLabelOption):
            return True

        return self.to_dict() != other.to_dict()
