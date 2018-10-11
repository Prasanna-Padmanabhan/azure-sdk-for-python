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

from .resource import Resource


class VirtualHub(Resource):
    """VirtualHub Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param virtual_wan: The VirtualWAN to which the VirtualHub belongs
    :type virtual_wan: ~azure.mgmt.network.v2018_07_01.models.SubResource
    :param hub_virtual_network_connections: list of all vnet connections with
     this VirtualHub.
    :type hub_virtual_network_connections:
     list[~azure.mgmt.network.v2018_07_01.models.HubVirtualNetworkConnection]
    :param address_prefix: Address-prefix for this VirtualHub.
    :type address_prefix: str
    :param provisioning_state: The provisioning state of the resource.
     Possible values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :type provisioning_state: str or
     ~azure.mgmt.network.v2018_07_01.models.ProvisioningState
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'virtual_wan': {'key': 'properties.virtualWan', 'type': 'SubResource'},
        'hub_virtual_network_connections': {'key': 'properties.hubVirtualNetworkConnections', 'type': '[HubVirtualNetworkConnection]'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualHub, self).__init__(**kwargs)
        self.virtual_wan = kwargs.get('virtual_wan', None)
        self.hub_virtual_network_connections = kwargs.get('hub_virtual_network_connections', None)
        self.address_prefix = kwargs.get('address_prefix', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.etag = None
