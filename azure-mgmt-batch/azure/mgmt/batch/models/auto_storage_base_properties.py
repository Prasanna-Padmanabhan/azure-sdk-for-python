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


class AutoStorageBaseProperties(Model):
    """The properties related to the auto-storage account.

    :param storage_account_id: The resource ID of the storage account to be
     used for auto-storage account.
    :type storage_account_id: str
    """

    _validation = {
        'storage_account_id': {'required': True},
    }

    _attribute_map = {
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
    }

    def __init__(self, storage_account_id):
        super(AutoStorageBaseProperties, self).__init__()
        self.storage_account_id = storage_account_id
