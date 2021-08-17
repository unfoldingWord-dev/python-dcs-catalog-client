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


class IssueLabelsOption(object):
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
        'labels': 'list[int]'
    }

    attribute_map = {
        'labels': 'labels'
    }

    def __init__(self, labels=None, _configuration=None):  # noqa: E501
        """IssueLabelsOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._labels = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels

    @property
    def labels(self):
        """Gets the labels of this IssueLabelsOption.  # noqa: E501

        list of label IDs  # noqa: E501

        :return: The labels of this IssueLabelsOption.  # noqa: E501
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IssueLabelsOption.

        list of label IDs  # noqa: E501

        :param labels: The labels of this IssueLabelsOption.  # noqa: E501
        :type: list[int]
        """

        self._labels = labels

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
        if issubclass(IssueLabelsOption, dict):
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
        if not isinstance(other, IssueLabelsOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IssueLabelsOption):
            return True

        return self.to_dict() != other.to_dict()
