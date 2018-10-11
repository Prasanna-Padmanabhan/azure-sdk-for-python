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

from .proxy_only_resource_py3 import ProxyOnlyResource


class PremierAddOnPatchResource(ProxyOnlyResource):
    """ARM resource for a PremierAddOn.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param sku: Premier add on SKU.
    :type sku: str
    :param product: Premier add on Product.
    :type product: str
    :param vendor: Premier add on Vendor.
    :type vendor: str
    :param marketplace_publisher: Premier add on Marketplace publisher.
    :type marketplace_publisher: str
    :param marketplace_offer: Premier add on Marketplace offer.
    :type marketplace_offer: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'str'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'vendor': {'key': 'properties.vendor', 'type': 'str'},
        'marketplace_publisher': {'key': 'properties.marketplacePublisher', 'type': 'str'},
        'marketplace_offer': {'key': 'properties.marketplaceOffer', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, sku: str=None, product: str=None, vendor: str=None, marketplace_publisher: str=None, marketplace_offer: str=None, **kwargs) -> None:
        super(PremierAddOnPatchResource, self).__init__(kind=kind, **kwargs)
        self.sku = sku
        self.product = product
        self.vendor = vendor
        self.marketplace_publisher = marketplace_publisher
        self.marketplace_offer = marketplace_offer
