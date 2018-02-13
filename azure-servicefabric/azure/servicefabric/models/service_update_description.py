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


class ServiceUpdateDescription(Model):
    """A ServiceUpdateDescription contains all of the information necessary to
    update a service.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StatefulServiceUpdateDescription,
    StatelessServiceUpdateDescription

    :param flags: Flags indicating whether other properties are set. Each of
     the associated properties corresponds to a flag, specified below, which,
     if set, indicate that the property is specified.
     This property can be a combination of those flags obtained using bitwise
     'OR' operator.
     For example, if the provided value is 6 then the flags for
     ReplicaRestartWaitDuration (2) and QuorumLossWaitDuration (4) are set.
     - None - Does not indicate any other properties are set. The value is
     zero.
     - TargetReplicaSetSize/InstanceCount - Indicates whether the
     TargetReplicaSetSize property (for Stateful services) or the InstanceCount
     property (for Stateless services) is set. The value is 1.
     - ReplicaRestartWaitDuration - Indicates the ReplicaRestartWaitDuration
     property is set. The value is  2.
     - QuorumLossWaitDuration - Indicates the QuorumLossWaitDuration property
     is set. The value is 4.
     - StandByReplicaKeepDuration - Indicates the StandByReplicaKeepDuration
     property is set. The value is 8.
     - MinReplicaSetSize - Indicates the MinReplicaSetSize property is set. The
     value is 16.
     - PlacementConstraints - Indicates the PlacementConstraints property is
     set. The value is 32.
     - PlacementPolicyList - Indicates the ServicePlacementPolicies property is
     set. The value is 64.
     - Correlation - Indicates the CorrelationScheme property is set. The value
     is 128.
     - Metrics - Indicates the ServiceLoadMetrics property is set. The value is
     256.
     - DefaultMoveCost - Indicates the DefaultMoveCost property is set. The
     value is 512.
    :type flags: str
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: The correlation scheme.
    :type correlation_scheme:
     list[~azure.servicefabric.models.ServiceCorrelationDescription]
    :param load_metrics: The service load metrics.
    :type load_metrics:
     list[~azure.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies: The service placement policies.
    :type service_placement_policies:
     list[~azure.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: The move cost for the service. Possible values
     include: 'Zero', 'Low', 'Medium', 'High'
    :type default_move_cost: str or ~azure.servicefabric.models.MoveCost
    :param service_kind: Constant filled by server.
    :type service_kind: str
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'flags': {'key': 'Flags', 'type': 'str'},
        'placement_constraints': {'key': 'PlacementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'CorrelationScheme', 'type': '[ServiceCorrelationDescription]'},
        'load_metrics': {'key': 'LoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'ServicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'DefaultMoveCost', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
    }

    _subtype_map = {
        'service_kind': {'Stateful': 'StatefulServiceUpdateDescription', 'Stateless': 'StatelessServiceUpdateDescription'}
    }

    def __init__(self, flags=None, placement_constraints=None, correlation_scheme=None, load_metrics=None, service_placement_policies=None, default_move_cost=None):
        super(ServiceUpdateDescription, self).__init__()
        self.flags = flags
        self.placement_constraints = placement_constraints
        self.correlation_scheme = correlation_scheme
        self.load_metrics = load_metrics
        self.service_placement_policies = service_placement_policies
        self.default_move_cost = default_move_cost
        self.service_kind = None
