# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.20
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1TokenRequestSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'audiences': 'list[str]',
        'bound_object_ref': 'V1BoundObjectReference',
        'expiration_seconds': 'int'
    }

    attribute_map = {
        'audiences': 'audiences',
        'bound_object_ref': 'boundObjectRef',
        'expiration_seconds': 'expirationSeconds'
    }

    def __init__(self, audiences=None, bound_object_ref=None, expiration_seconds=None, local_vars_configuration=None):  # noqa: E501
        """V1TokenRequestSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audiences = None
        self._bound_object_ref = None
        self._expiration_seconds = None
        self.discriminator = None

        self.audiences = audiences
        if bound_object_ref is not None:
            self.bound_object_ref = bound_object_ref
        if expiration_seconds is not None:
            self.expiration_seconds = expiration_seconds

    @property
    def audiences(self):
        """Gets the audiences of this V1TokenRequestSpec.  # noqa: E501

        Audiences are the intendend audiences of the token. A recipient of a token must identitfy themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.  # noqa: E501

        :return: The audiences of this V1TokenRequestSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._audiences

    @audiences.setter
    def audiences(self, audiences):
        """Sets the audiences of this V1TokenRequestSpec.

        Audiences are the intendend audiences of the token. A recipient of a token must identitfy themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.  # noqa: E501

        :param audiences: The audiences of this V1TokenRequestSpec.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and audiences is None:  # noqa: E501
            raise ValueError("Invalid value for `audiences`, must not be `None`")  # noqa: E501

        self._audiences = audiences

    @property
    def bound_object_ref(self):
        """Gets the bound_object_ref of this V1TokenRequestSpec.  # noqa: E501


        :return: The bound_object_ref of this V1TokenRequestSpec.  # noqa: E501
        :rtype: V1BoundObjectReference
        """
        return self._bound_object_ref

    @bound_object_ref.setter
    def bound_object_ref(self, bound_object_ref):
        """Sets the bound_object_ref of this V1TokenRequestSpec.


        :param bound_object_ref: The bound_object_ref of this V1TokenRequestSpec.  # noqa: E501
        :type: V1BoundObjectReference
        """

        self._bound_object_ref = bound_object_ref

    @property
    def expiration_seconds(self):
        """Gets the expiration_seconds of this V1TokenRequestSpec.  # noqa: E501

        ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.  # noqa: E501

        :return: The expiration_seconds of this V1TokenRequestSpec.  # noqa: E501
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """Sets the expiration_seconds of this V1TokenRequestSpec.

        ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.  # noqa: E501

        :param expiration_seconds: The expiration_seconds of this V1TokenRequestSpec.  # noqa: E501
        :type: int
        """

        self._expiration_seconds = expiration_seconds

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1TokenRequestSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TokenRequestSpec):
            return True

        return self.to_dict() != other.to_dict()
