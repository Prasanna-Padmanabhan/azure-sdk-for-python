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


class WorkspacesListOptions(Model):
    """Additional parameters for list operation.

    :param max_results: The maximum number of items to return in the response.
     A maximum of 1000 files can be returned. Default value: 1000 .
    :type max_results: int
    """

    _attribute_map = {
        'max_results': {'key': '', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(WorkspacesListOptions, self).__init__(**kwargs)
        self.max_results = kwargs.get('max_results', 1000)
