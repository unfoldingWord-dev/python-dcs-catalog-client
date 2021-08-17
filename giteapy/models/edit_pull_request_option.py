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


class EditPullRequestOption(object):
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
        'assignee': 'str',
        'assignees': 'list[str]',
        'base': 'str',
        'body': 'str',
        'due_date': 'datetime',
        'labels': 'list[int]',
        'milestone': 'int',
        'state': 'str',
        'title': 'str',
        'unset_due_date': 'bool'
    }

    attribute_map = {
        'assignee': 'assignee',
        'assignees': 'assignees',
        'base': 'base',
        'body': 'body',
        'due_date': 'due_date',
        'labels': 'labels',
        'milestone': 'milestone',
        'state': 'state',
        'title': 'title',
        'unset_due_date': 'unset_due_date'
    }

    def __init__(self, assignee=None, assignees=None, base=None, body=None, due_date=None, labels=None, milestone=None, state=None, title=None, unset_due_date=None, _configuration=None):  # noqa: E501
        """EditPullRequestOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assignee = None
        self._assignees = None
        self._base = None
        self._body = None
        self._due_date = None
        self._labels = None
        self._milestone = None
        self._state = None
        self._title = None
        self._unset_due_date = None
        self.discriminator = None

        if assignee is not None:
            self.assignee = assignee
        if assignees is not None:
            self.assignees = assignees
        if base is not None:
            self.base = base
        if body is not None:
            self.body = body
        if due_date is not None:
            self.due_date = due_date
        if labels is not None:
            self.labels = labels
        if milestone is not None:
            self.milestone = milestone
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if unset_due_date is not None:
            self.unset_due_date = unset_due_date

    @property
    def assignee(self):
        """Gets the assignee of this EditPullRequestOption.  # noqa: E501


        :return: The assignee of this EditPullRequestOption.  # noqa: E501
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this EditPullRequestOption.


        :param assignee: The assignee of this EditPullRequestOption.  # noqa: E501
        :type: str
        """

        self._assignee = assignee

    @property
    def assignees(self):
        """Gets the assignees of this EditPullRequestOption.  # noqa: E501


        :return: The assignees of this EditPullRequestOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        """Sets the assignees of this EditPullRequestOption.


        :param assignees: The assignees of this EditPullRequestOption.  # noqa: E501
        :type: list[str]
        """

        self._assignees = assignees

    @property
    def base(self):
        """Gets the base of this EditPullRequestOption.  # noqa: E501


        :return: The base of this EditPullRequestOption.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this EditPullRequestOption.


        :param base: The base of this EditPullRequestOption.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def body(self):
        """Gets the body of this EditPullRequestOption.  # noqa: E501


        :return: The body of this EditPullRequestOption.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EditPullRequestOption.


        :param body: The body of this EditPullRequestOption.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def due_date(self):
        """Gets the due_date of this EditPullRequestOption.  # noqa: E501


        :return: The due_date of this EditPullRequestOption.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this EditPullRequestOption.


        :param due_date: The due_date of this EditPullRequestOption.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def labels(self):
        """Gets the labels of this EditPullRequestOption.  # noqa: E501


        :return: The labels of this EditPullRequestOption.  # noqa: E501
        :rtype: list[int]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this EditPullRequestOption.


        :param labels: The labels of this EditPullRequestOption.  # noqa: E501
        :type: list[int]
        """

        self._labels = labels

    @property
    def milestone(self):
        """Gets the milestone of this EditPullRequestOption.  # noqa: E501


        :return: The milestone of this EditPullRequestOption.  # noqa: E501
        :rtype: int
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        """Sets the milestone of this EditPullRequestOption.


        :param milestone: The milestone of this EditPullRequestOption.  # noqa: E501
        :type: int
        """

        self._milestone = milestone

    @property
    def state(self):
        """Gets the state of this EditPullRequestOption.  # noqa: E501


        :return: The state of this EditPullRequestOption.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EditPullRequestOption.


        :param state: The state of this EditPullRequestOption.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this EditPullRequestOption.  # noqa: E501


        :return: The title of this EditPullRequestOption.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EditPullRequestOption.


        :param title: The title of this EditPullRequestOption.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def unset_due_date(self):
        """Gets the unset_due_date of this EditPullRequestOption.  # noqa: E501


        :return: The unset_due_date of this EditPullRequestOption.  # noqa: E501
        :rtype: bool
        """
        return self._unset_due_date

    @unset_due_date.setter
    def unset_due_date(self, unset_due_date):
        """Sets the unset_due_date of this EditPullRequestOption.


        :param unset_due_date: The unset_due_date of this EditPullRequestOption.  # noqa: E501
        :type: bool
        """

        self._unset_due_date = unset_due_date

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
        if issubclass(EditPullRequestOption, dict):
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
        if not isinstance(other, EditPullRequestOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditPullRequestOption):
            return True

        return self.to_dict() != other.to_dict()
