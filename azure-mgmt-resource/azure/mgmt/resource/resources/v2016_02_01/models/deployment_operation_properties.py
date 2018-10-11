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


class DeploymentOperationProperties(Model):
    """Deployment operation properties.

    :param provisioning_state: The state of the provisioning.
    :type provisioning_state: str
    :param timestamp: The date and time of the operation.
    :type timestamp: datetime
    :param service_request_id: Deployment operation service request id.
    :type service_request_id: str
    :param status_code: Operation status code.
    :type status_code: str
    :param status_message: Operation status message.
    :type status_message: object
    :param target_resource: The target resource.
    :type target_resource:
     ~azure.mgmt.resource.resources.v2016_02_01.models.TargetResource
    :param request: The HTTP request message.
    :type request:
     ~azure.mgmt.resource.resources.v2016_02_01.models.HttpMessage
    :param response: The HTTP response message.
    :type response:
     ~azure.mgmt.resource.resources.v2016_02_01.models.HttpMessage
    """

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'service_request_id': {'key': 'serviceRequestId', 'type': 'str'},
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'object'},
        'target_resource': {'key': 'targetResource', 'type': 'TargetResource'},
        'request': {'key': 'request', 'type': 'HttpMessage'},
        'response': {'key': 'response', 'type': 'HttpMessage'},
    }

    def __init__(self, **kwargs):
        super(DeploymentOperationProperties, self).__init__(**kwargs)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.timestamp = kwargs.get('timestamp', None)
        self.service_request_id = kwargs.get('service_request_id', None)
        self.status_code = kwargs.get('status_code', None)
        self.status_message = kwargs.get('status_message', None)
        self.target_resource = kwargs.get('target_resource', None)
        self.request = kwargs.get('request', None)
        self.response = kwargs.get('response', None)
