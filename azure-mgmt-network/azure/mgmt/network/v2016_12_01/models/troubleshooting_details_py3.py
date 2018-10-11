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


class TroubleshootingDetails(Model):
    """Information gained from troubleshooting of specified resource.

    :param id: The id of the get troubleshoot operation.
    :type id: str
    :param reason_type: Reason type of failure.
    :type reason_type: str
    :param summary: A summary of troubleshooting.
    :type summary: str
    :param detail: Details on troubleshooting results.
    :type detail: str
    :param recommended_actions: List of recommended actions.
    :type recommended_actions:
     list[~azure.mgmt.network.v2016_12_01.models.TroubleshootingRecommendedActions]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'reason_type': {'key': 'reasonType', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        'detail': {'key': 'detail', 'type': 'str'},
        'recommended_actions': {'key': 'recommendedActions', 'type': '[TroubleshootingRecommendedActions]'},
    }

    def __init__(self, *, id: str=None, reason_type: str=None, summary: str=None, detail: str=None, recommended_actions=None, **kwargs) -> None:
        super(TroubleshootingDetails, self).__init__(**kwargs)
        self.id = id
        self.reason_type = reason_type
        self.summary = summary
        self.detail = detail
        self.recommended_actions = recommended_actions
