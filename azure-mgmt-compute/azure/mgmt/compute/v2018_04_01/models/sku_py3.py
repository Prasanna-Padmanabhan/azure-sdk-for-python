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


class Sku(Model):
    """Describes a virtual machine scale set sku.

    :param name: The sku name.
    :type name: str
    :param tier: Specifies the tier of virtual machines in a scale set.<br
     /><br /> Possible Values:<br /><br /> **Standard**<br /><br /> **Basic**
    :type tier: str
    :param capacity: Specifies the number of virtual machines in the scale
     set.
    :type capacity: long
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'long'},
    }

    def __init__(self, *, name: str=None, tier: str=None, capacity: int=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
        self.capacity = capacity
