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


class SubnetFragment(Model):
    """Subnet information.

    :param resource_id: The resource ID of the subnet.
    :type resource_id: str
    :param lab_subnet_name: The name of the subnet as seen in the lab.
    :type lab_subnet_name: str
    :param allow_public_ip: The permission policy of the subnet for allowing
     public IP addresses (i.e. Allow, Deny)). Possible values include:
     'Default', 'Deny', 'Allow'
    :type allow_public_ip: str or
     ~azure.mgmt.devtestlabs.models.UsagePermissionType
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'lab_subnet_name': {'key': 'labSubnetName', 'type': 'str'},
        'allow_public_ip': {'key': 'allowPublicIp', 'type': 'str'},
    }

    def __init__(self, resource_id=None, lab_subnet_name=None, allow_public_ip=None):
        super(SubnetFragment, self).__init__()
        self.resource_id = resource_id
        self.lab_subnet_name = lab_subnet_name
        self.allow_public_ip = allow_public_ip
