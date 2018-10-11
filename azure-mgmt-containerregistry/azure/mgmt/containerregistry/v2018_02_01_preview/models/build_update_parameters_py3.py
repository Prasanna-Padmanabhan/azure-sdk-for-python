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


class BuildUpdateParameters(Model):
    """The set of build properties that can be updated.

    :param is_archive_enabled: The value that indicates whether archiving is
     enabled or not.
    :type is_archive_enabled: bool
    """

    _attribute_map = {
        'is_archive_enabled': {'key': 'isArchiveEnabled', 'type': 'bool'},
    }

    def __init__(self, *, is_archive_enabled: bool=None, **kwargs) -> None:
        super(BuildUpdateParameters, self).__init__(**kwargs)
        self.is_archive_enabled = is_archive_enabled
