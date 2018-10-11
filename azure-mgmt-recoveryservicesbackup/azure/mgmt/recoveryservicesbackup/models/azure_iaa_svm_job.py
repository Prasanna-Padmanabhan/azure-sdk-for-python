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

from .job import Job


class AzureIaaSVMJob(Job):
    """Azure IaaS VM workload-specifc job object.

    All required parameters must be populated in order to send to Azure.

    :param entity_friendly_name: Friendly name of the entity on which the
     current job is executing.
    :type entity_friendly_name: str
    :param backup_management_type: Backup management type to execute the
     current job. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param operation: The operation name.
    :type operation: str
    :param status: Job status.
    :type status: str
    :param start_time: The start time.
    :type start_time: datetime
    :param end_time: The end time.
    :type end_time: datetime
    :param activity_id: ActivityId of job.
    :type activity_id: str
    :param job_type: Required. Constant filled by server.
    :type job_type: str
    :param duration: Time elapsed during the execution of this job.
    :type duration: timedelta
    :param actions_info: Gets or sets the state/actions applicable on this job
     like cancel/retry.
    :type actions_info: list[str or
     ~azure.mgmt.recoveryservicesbackup.models.JobSupportedAction]
    :param error_details: Error details on execution of this job.
    :type error_details:
     list[~azure.mgmt.recoveryservicesbackup.models.AzureIaaSVMErrorInfo]
    :param virtual_machine_version: Specifies whether the backup item is a
     Classic or an Azure Resource Manager VM.
    :type virtual_machine_version: str
    :param extended_info: Additional information for this job.
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.AzureIaaSVMJobExtendedInfo
    """

    _validation = {
        'job_type': {'required': True},
    }

    _attribute_map = {
        'entity_friendly_name': {'key': 'entityFriendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'duration'},
        'actions_info': {'key': 'actionsInfo', 'type': '[JobSupportedAction]'},
        'error_details': {'key': 'errorDetails', 'type': '[AzureIaaSVMErrorInfo]'},
        'virtual_machine_version': {'key': 'virtualMachineVersion', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AzureIaaSVMJobExtendedInfo'},
    }

    def __init__(self, **kwargs):
        super(AzureIaaSVMJob, self).__init__(**kwargs)
        self.duration = kwargs.get('duration', None)
        self.actions_info = kwargs.get('actions_info', None)
        self.error_details = kwargs.get('error_details', None)
        self.virtual_machine_version = kwargs.get('virtual_machine_version', None)
        self.extended_info = kwargs.get('extended_info', None)
        self.job_type = 'AzureIaaSVMJob'
