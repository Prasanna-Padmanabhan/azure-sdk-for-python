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


class ClientCertificateCommonName(Model):
    """Describes the client certificate details using common name.

    All required parameters must be populated in order to send to Azure.

    :param is_admin: Required. Indicates if the client certificate has admin
     access to the cluster. Non admin clients can perform only read only
     operations on the cluster.
    :type is_admin: bool
    :param certificate_common_name: Required. The common name of the client
     certificate.
    :type certificate_common_name: str
    :param certificate_issuer_thumbprint: Required. The issuer thumbprint of
     the client certificate.
    :type certificate_issuer_thumbprint: str
    """

    _validation = {
        'is_admin': {'required': True},
        'certificate_common_name': {'required': True},
        'certificate_issuer_thumbprint': {'required': True},
    }

    _attribute_map = {
        'is_admin': {'key': 'isAdmin', 'type': 'bool'},
        'certificate_common_name': {'key': 'certificateCommonName', 'type': 'str'},
        'certificate_issuer_thumbprint': {'key': 'certificateIssuerThumbprint', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ClientCertificateCommonName, self).__init__(**kwargs)
        self.is_admin = kwargs.get('is_admin', None)
        self.certificate_common_name = kwargs.get('certificate_common_name', None)
        self.certificate_issuer_thumbprint = kwargs.get('certificate_issuer_thumbprint', None)
