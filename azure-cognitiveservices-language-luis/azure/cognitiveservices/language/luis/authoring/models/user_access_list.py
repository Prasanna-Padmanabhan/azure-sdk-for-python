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


class UserAccessList(Model):
    """List of user permissions.

    :param owner: The email address of owner of the application.
    :type owner: str
    :param emails:
    :type emails: list[str]
    """

    _attribute_map = {
        'owner': {'key': 'owner', 'type': 'str'},
        'emails': {'key': 'emails', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(UserAccessList, self).__init__(**kwargs)
        self.owner = kwargs.get('owner', None)
        self.emails = kwargs.get('emails', None)
