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


class ResourceMetric(Model):
    """Object representing a metric for any resource .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of metric.
    :vartype name: ~azure.mgmt.web.models.ResourceMetricName
    :ivar unit: Metric unit.
    :vartype unit: str
    :ivar time_grain: Metric granularity. E.g PT1H, PT5M, P1D
    :vartype time_grain: str
    :ivar start_time: Metric start time.
    :vartype start_time: datetime
    :ivar end_time: Metric end time.
    :vartype end_time: datetime
    :ivar resource_id: Metric resource Id.
    :vartype resource_id: str
    :ivar id: Resource Id.
    :vartype id: str
    :ivar metric_values: Metric values.
    :vartype metric_values: list[~azure.mgmt.web.models.ResourceMetricValue]
    :ivar properties: Resource metric properties collection.
    :vartype properties: list[~azure.mgmt.web.models.ResourceMetricProperty]
    """

    _validation = {
        'name': {'readonly': True},
        'unit': {'readonly': True},
        'time_grain': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'resource_id': {'readonly': True},
        'id': {'readonly': True},
        'metric_values': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'ResourceMetricName'},
        'unit': {'key': 'unit', 'type': 'str'},
        'time_grain': {'key': 'timeGrain', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'metric_values': {'key': 'metricValues', 'type': '[ResourceMetricValue]'},
        'properties': {'key': 'properties', 'type': '[ResourceMetricProperty]'},
    }

    def __init__(self, **kwargs):
        super(ResourceMetric, self).__init__(**kwargs)
        self.name = None
        self.unit = None
        self.time_grain = None
        self.start_time = None
        self.end_time = None
        self.resource_id = None
        self.id = None
        self.metric_values = None
        self.properties = None
