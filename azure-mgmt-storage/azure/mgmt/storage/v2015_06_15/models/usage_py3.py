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


class Usage(Model):
    """Describes Storage Resource Usage.

    All required parameters must be populated in order to send to Azure.

    :param unit: Required. The unit of measurement. Possible values include:
     'Count', 'Bytes', 'Seconds', 'Percent', 'CountsPerSecond',
     'BytesPerSecond'
    :type unit: str or ~azure.mgmt.storage.v2015_06_15.models.UsageUnit
    :param current_value: Required. The current count of the allocated
     resources in the subscription.
    :type current_value: int
    :param limit: Required. The maximum count of the resources that can be
     allocated in the subscription.
    :type limit: int
    :param name: Required. The name of the type of usage.
    :type name: ~azure.mgmt.storage.v2015_06_15.models.UsageName
    """

    _validation = {
        'unit': {'required': True},
        'current_value': {'required': True},
        'limit': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'UsageUnit'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(self, *, unit, current_value: int, limit: int, name, **kwargs) -> None:
        super(Usage, self).__init__(**kwargs)
        self.unit = unit
        self.current_value = current_value
        self.limit = limit
        self.name = name
