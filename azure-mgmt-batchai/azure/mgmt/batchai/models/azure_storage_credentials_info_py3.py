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

from msrest.serialization import Model


class AzureStorageCredentialsInfo(Model):
    """Credentials to access Azure File Share.

    :param account_key: Storage account key. One of accountKey or
     accountKeySecretReference must be specified.
    :type account_key: str
    :param account_key_secret_reference: Specifies the location of the storage
     account key, which is a Key Vault Secret. Users can store their secrets in
     Azure KeyVault and pass it to the Batch AI Service to integrate with
     KeyVault. One of accountKey or accountKeySecretReference must be
     specified.
    :type account_key_secret_reference:
     ~azure.mgmt.batchai.models.KeyVaultSecretReference
    """

    _attribute_map = {
        'account_key': {'key': 'accountKey', 'type': 'str'},
        'account_key_secret_reference': {'key': 'accountKeySecretReference', 'type': 'KeyVaultSecretReference'},
    }

    def __init__(self, *, account_key: str=None, account_key_secret_reference=None, **kwargs) -> None:
        super(AzureStorageCredentialsInfo, self).__init__(**kwargs)
        self.account_key = account_key
        self.account_key_secret_reference = account_key_secret_reference
