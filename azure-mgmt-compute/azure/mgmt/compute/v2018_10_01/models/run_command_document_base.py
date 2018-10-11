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


class RunCommandDocumentBase(Model):
    """Describes the properties of a Run Command metadata.

    All required parameters must be populated in order to send to Azure.

    :param schema: Required. The VM run command schema.
    :type schema: str
    :param id: Required. The VM run command id.
    :type id: str
    :param os_type: Required. The Operating System type. Possible values
     include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_10_01.models.OperatingSystemTypes
    :param label: Required. The VM run command label.
    :type label: str
    :param description: Required. The VM run command description.
    :type description: str
    """

    _validation = {
        'schema': {'required': True},
        'id': {'required': True},
        'os_type': {'required': True},
        'label': {'required': True},
        'description': {'required': True},
    }

    _attribute_map = {
        'schema': {'key': '$schema', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'label': {'key': 'label', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RunCommandDocumentBase, self).__init__(**kwargs)
        self.schema = kwargs.get('schema', None)
        self.id = kwargs.get('id', None)
        self.os_type = kwargs.get('os_type', None)
        self.label = kwargs.get('label', None)
        self.description = kwargs.get('description', None)
