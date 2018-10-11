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


class BoundingBox(Model):
    """BoundingBox.

    :param left:
    :type left: float
    :param top:
    :type top: float
    :param width:
    :type width: float
    :param height:
    :type height: float
    """

    _attribute_map = {
        'left': {'key': 'left', 'type': 'float'},
        'top': {'key': 'top', 'type': 'float'},
        'width': {'key': 'width', 'type': 'float'},
        'height': {'key': 'height', 'type': 'float'},
    }

    def __init__(self, *, left: float=None, top: float=None, width: float=None, height: float=None, **kwargs) -> None:
        super(BoundingBox, self).__init__(**kwargs)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
