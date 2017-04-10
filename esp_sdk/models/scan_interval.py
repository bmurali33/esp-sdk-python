# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class ScanInterval(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, relationships=None, errors=None, id=None, created_at=None, interval=None, updated_at=None, external_account=None, external_account_id=None, service=None, service_id=None):
        """
        ScanInterval - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'relationships': 'object',
            'errors': 'list[str]',
            'id': 'int',
            'created_at': 'datetime',
            'interval': 'int',
            'updated_at': 'datetime',
            'external_account': 'ExternalAccount',
            'external_account_id': 'int',
            'service': 'Service',
            'service_id': 'int'
        }

        self.attribute_map = {
            'relationships': 'relationships',
            'errors': 'errors',
            'id': 'id',
            'created_at': 'created_at',
            'interval': 'interval',
            'updated_at': 'updated_at',
            'external_account': 'external_account',
            'external_account_id': 'external_account_id',
            'service': 'service',
            'service_id': 'service_id'
        }

        self._relationships = relationships
        self._errors = errors
        self._id = id
        self._created_at = created_at
        self._interval = interval
        self._updated_at = updated_at
        self._external_account = external_account
        self._external_account_id = external_account_id
        self._service = service
        self._service_id = service_id

    @property
    def relationships(self):
        """
        Gets the relationships of this ScanInterval.
        Links to Associated Objects

        :return: The relationships of this ScanInterval.
        :rtype: object
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this ScanInterval.
        Links to Associated Objects

        :param relationships: The relationships of this ScanInterval.
        :type: object
        """

        self._relationships = relationships

    @property
    def errors(self):
        """
        Gets the errors of this ScanInterval.
        Array of error messages if the request failed

        :return: The errors of this ScanInterval.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ScanInterval.
        Array of error messages if the request failed

        :param errors: The errors of this ScanInterval.
        :type: list[str]
        """

        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this ScanInterval.
        Unique ID

        :return: The id of this ScanInterval.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScanInterval.
        Unique ID

        :param id: The id of this ScanInterval.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this ScanInterval.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this ScanInterval.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ScanInterval.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this ScanInterval.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def interval(self):
        """
        Gets the interval of this ScanInterval.
        The interval, in minutes, this service will be scanned

        :return: The interval of this ScanInterval.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ScanInterval.
        The interval, in minutes, this service will be scanned

        :param interval: The interval of this ScanInterval.
        :type: int
        """

        self._interval = interval

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ScanInterval.
        ISO 8601 timestamp when the resource was last updated

        :return: The updated_at of this ScanInterval.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ScanInterval.
        ISO 8601 timestamp when the resource was last updated

        :param updated_at: The updated_at of this ScanInterval.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def external_account(self):
        """
        Gets the external_account of this ScanInterval.
        Associated External Account

        :return: The external_account of this ScanInterval.
        :rtype: ExternalAccount
        """
        return self._external_account

    @external_account.setter
    def external_account(self, external_account):
        """
        Sets the external_account of this ScanInterval.
        Associated External Account

        :param external_account: The external_account of this ScanInterval.
        :type: ExternalAccount
        """

        self._external_account = external_account

    @property
    def external_account_id(self):
        """
        Gets the external_account_id of this ScanInterval.
        Associated External Account Id

        :return: The external_account_id of this ScanInterval.
        :rtype: int
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """
        Sets the external_account_id of this ScanInterval.
        Associated External Account Id

        :param external_account_id: The external_account_id of this ScanInterval.
        :type: int
        """

        self._external_account_id = external_account_id

    @property
    def service(self):
        """
        Gets the service of this ScanInterval.
        Associated Service

        :return: The service of this ScanInterval.
        :rtype: Service
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this ScanInterval.
        Associated Service

        :param service: The service of this ScanInterval.
        :type: Service
        """

        self._service = service

    @property
    def service_id(self):
        """
        Gets the service_id of this ScanInterval.
        Associated Service Id

        :return: The service_id of this ScanInterval.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """
        Sets the service_id of this ScanInterval.
        Associated Service Id

        :param service_id: The service_id of this ScanInterval.
        :type: int
        """

        self._service_id = service_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ScanInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other