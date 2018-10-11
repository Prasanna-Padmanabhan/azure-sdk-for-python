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


class ClusterHealthPolicy(Model):
    """Defines a health policy used to evaluate the health of the cluster or of a
    cluster node.

    :param max_percent_unhealthy_nodes: The maximum allowed percentage of
     unhealthy nodes before reporting an error. For example, to allow 10% of
     nodes to be unhealthy, this value would be 10.
    :type max_percent_unhealthy_nodes: int
    :param max_percent_unhealthy_applications: The maximum allowed percentage
     of unhealthy applications before reporting an error. For example, to allow
     10% of applications to be unhealthy, this value would be 10.
    :type max_percent_unhealthy_applications: int
    """

    _validation = {
        'max_percent_unhealthy_nodes': {'maximum': 100, 'minimum': 0},
        'max_percent_unhealthy_applications': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'max_percent_unhealthy_nodes': {'key': 'maxPercentUnhealthyNodes', 'type': 'int'},
        'max_percent_unhealthy_applications': {'key': 'maxPercentUnhealthyApplications', 'type': 'int'},
    }

    def __init__(self, *, max_percent_unhealthy_nodes: int=None, max_percent_unhealthy_applications: int=None, **kwargs) -> None:
        super(ClusterHealthPolicy, self).__init__(**kwargs)
        self.max_percent_unhealthy_nodes = max_percent_unhealthy_nodes
        self.max_percent_unhealthy_applications = max_percent_unhealthy_applications
