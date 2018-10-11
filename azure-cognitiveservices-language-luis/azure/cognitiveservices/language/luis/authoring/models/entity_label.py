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


class EntityLabel(Model):
    """Defines the entity type and position of the extracted entity within the
    example.

    All required parameters must be populated in order to send to Azure.

    :param entity_name: Required. The entity type.
    :type entity_name: str
    :param start_token_index: Required. The index within the utterance where
     the extracted entity starts.
    :type start_token_index: int
    :param end_token_index: Required. The index within the utterance where the
     extracted entity ends.
    :type end_token_index: int
    """

    _validation = {
        'entity_name': {'required': True},
        'start_token_index': {'required': True},
        'end_token_index': {'required': True},
    }

    _attribute_map = {
        'entity_name': {'key': 'entityName', 'type': 'str'},
        'start_token_index': {'key': 'startTokenIndex', 'type': 'int'},
        'end_token_index': {'key': 'endTokenIndex', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(EntityLabel, self).__init__(**kwargs)
        self.entity_name = kwargs.get('entity_name', None)
        self.start_token_index = kwargs.get('start_token_index', None)
        self.end_token_index = kwargs.get('end_token_index', None)
