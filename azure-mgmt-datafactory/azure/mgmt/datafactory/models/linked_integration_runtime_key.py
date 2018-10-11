# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_integration_runtime_properties import LinkedIntegrationRuntimeProperties


class LinkedIntegrationRuntimeKey(LinkedIntegrationRuntimeProperties):
    """The base definition of a secret type.

    :param authorization_type: Constant filled by server.
    :type authorization_type: str
    :param key: Type of the secret.
    :type key: ~azure.mgmt.datafactory.models.SecureString
    """

    _validation = {
        'authorization_type': {'required': True},
        'key': {'required': True},
    }

    _attribute_map = {
        'authorization_type': {'key': 'authorizationType', 'type': 'str'},
        'key': {'key': 'key', 'type': 'SecureString'},
    }

    def __init__(self, key):
        super(LinkedIntegrationRuntimeKey, self).__init__()
        self.key = key
        self.authorization_type = 'Key'
