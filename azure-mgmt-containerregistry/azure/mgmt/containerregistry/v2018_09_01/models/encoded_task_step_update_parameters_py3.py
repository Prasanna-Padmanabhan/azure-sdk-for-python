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

from .task_step_update_parameters_py3 import TaskStepUpdateParameters


class EncodedTaskStepUpdateParameters(TaskStepUpdateParameters):
    """The properties for updating encoded task step.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param encoded_task_content: Base64 encoded value of the
     template/definition file content.
    :type encoded_task_content: str
    :param encoded_values_content: Base64 encoded value of the
     parameters/values file content.
    :type encoded_values_content: str
    :param values: The collection of overridable values that can be passed
     when running a task.
    :type values:
     list[~azure.mgmt.containerregistry.v2018_09_01.models.SetValue]
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'encoded_task_content': {'key': 'encodedTaskContent', 'type': 'str'},
        'encoded_values_content': {'key': 'encodedValuesContent', 'type': 'str'},
        'values': {'key': 'values', 'type': '[SetValue]'},
    }

    def __init__(self, *, encoded_task_content: str=None, encoded_values_content: str=None, values=None, **kwargs) -> None:
        super(EncodedTaskStepUpdateParameters, self).__init__(**kwargs)
        self.encoded_task_content = encoded_task_content
        self.encoded_values_content = encoded_values_content
        self.values = values
        self.type = 'EncodedTask'
