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


class ExplicitListItemUpdateObject(Model):
    """Model object for updating an explicit list item.

    :param explicit_list_item: The explicit list item.
    :type explicit_list_item: str
    """

    _attribute_map = {
        'explicit_list_item': {'key': 'explicitListItem', 'type': 'str'},
    }

    def __init__(self, *, explicit_list_item: str=None, **kwargs) -> None:
        super(ExplicitListItemUpdateObject, self).__init__(**kwargs)
        self.explicit_list_item = explicit_list_item
