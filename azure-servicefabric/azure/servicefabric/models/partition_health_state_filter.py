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


class PartitionHealthStateFilter(Model):
    """Defines matching criteria to determine whether a partition should be
    included as a child of a service in the cluster health chunk.
    The partitions are only returned if the parent entities match a filter
    specified in the cluster health chunk query description. The parent service
    and application must be included in the cluster health chunk.
    One filter can match zero, one or multiple partitions, depending on its
    properties.
    .

    :param partition_id_filter: ID of the partition that matches the filter.
     The filter is applied only to the specified partition, if it exists.
     If the partition doesn't exist, no partition is returned in the cluster
     health chunk based on this filter.
     If the partition exists, it is included in the cluster health chunk if it
     respects the other filter properties.
     If not specified, all partitions that match the parent filters (if any)
     are taken into consideration and matched against the other filter members,
     like health state filter.
    :type partition_id_filter: str
    :param health_state_filter: The filter for the health state of the
     partitions. It allows selecting partitions if they match the desired
     health states.
     The possible values are integer value of one of the following health
     states. Only partitions that match the filter are returned. All partitions
     are used to evaluate the cluster aggregated health state.
     If not specified, default value is None, unless the partition id is
     specified. If the filter has default value and partition id is specified,
     the matching partition is returned.
     The state values are flag based enumeration, so the value could be a
     combination of these values obtained using bitwise 'OR' operator.
     For example, if the provided value is 6, it matches partitions with
     HealthState value of OK (2) and Warning (4).
     - Default - Default value. Matches any HealthState. The value is zero.
     - None - Filter that doesn't match any HealthState value. Used in order to
     return no results on a given collection of states. The value is 1.
     - Ok - Filter that matches input with HealthState value Ok. The value is
     2.
     - Warning - Filter that matches input with HealthState value Warning. The
     value is 4.
     - Error - Filter that matches input with HealthState value Error. The
     value is 8.
     - All - Filter that matches input with any HealthState value. The value is
     65535.
     . Default value: 0 .
    :type health_state_filter: int
    :param replica_filters: Defines a list of filters that specify which
     replicas to be included in the returned cluster health chunk as children
     of the parent partition. The replicas are returned only if the parent
     partition matches a filter.
     If the list is empty, no replicas are returned. All the replicas are used
     to evaluate the parent partition aggregated health state, regardless of
     the input filters.
     The partition filter may specify multiple replica filters.
     For example, it can specify a filter to return all replicas with health
     state Error and another filter to always include a replica identified by
     its replica id.
    :type replica_filters:
     list[~azure.servicefabric.models.ReplicaHealthStateFilter]
    """

    _attribute_map = {
        'partition_id_filter': {'key': 'PartitionIdFilter', 'type': 'str'},
        'health_state_filter': {'key': 'HealthStateFilter', 'type': 'int'},
        'replica_filters': {'key': 'ReplicaFilters', 'type': '[ReplicaHealthStateFilter]'},
    }

    def __init__(self, partition_id_filter=None, health_state_filter=0, replica_filters=None):
        super(PartitionHealthStateFilter, self).__init__()
        self.partition_id_filter = partition_id_filter
        self.health_state_filter = health_state_filter
        self.replica_filters = replica_filters
