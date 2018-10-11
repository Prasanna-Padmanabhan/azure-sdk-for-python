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

from .migrate_sql_server_sql_mi_task_output_py3 import MigrateSqlServerSqlMITaskOutput


class MigrateSqlServerSqlMITaskOutputMigrationLevel(MigrateSqlServerSqlMITaskOutput):
    """MigrateSqlServerSqlMITaskOutputMigrationLevel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar started_on: Migration start time
    :vartype started_on: datetime
    :ivar ended_on: Migration end time
    :vartype ended_on: datetime
    :ivar status: Current status of migration. Possible values include:
     'Default', 'Connecting', 'SourceAndTargetSelected', 'SelectLogins',
     'Configured', 'Running', 'Error', 'Stopped', 'Completed',
     'CompletedWithWarnings'
    :vartype status: str or ~azure.mgmt.datamigration.models.MigrationStatus
    :ivar state: Current state of migration. Possible values include: 'None',
     'InProgress', 'Failed', 'Warning', 'Completed', 'Skipped', 'Stopped'
    :vartype state: str or ~azure.mgmt.datamigration.models.MigrationState
    :ivar agent_jobs: Selected agent jobs as a map from name to id
    :vartype agent_jobs: dict[str, str]
    :ivar logins: Selected logins as a map from name to id
    :vartype logins: dict[str, str]
    :ivar message: Migration progress message
    :vartype message: str
    :ivar server_role_results: Map of server role migration results.
    :vartype server_role_results: dict[str,
     ~azure.mgmt.datamigration.models.StartMigrationScenarioServerRoleResult]
    :ivar orphaned_users: Map of users to database name of orphaned users.
    :vartype orphaned_users: dict[str, str]
    :ivar databases: Selected databases as a map from database name to
     database id
    :vartype databases: dict[str, str]
    :ivar source_server_version: Source server version
    :vartype source_server_version: str
    :ivar source_server_brand_version: Source server brand version
    :vartype source_server_brand_version: str
    :ivar target_server_version: Target server version
    :vartype target_server_version: str
    :ivar target_server_brand_version: Target server brand version
    :vartype target_server_brand_version: str
    :ivar exceptions_and_warnings: Migration exceptions and warnings.
    :vartype exceptions_and_warnings:
     list[~azure.mgmt.datamigration.models.ReportableException]
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'status': {'readonly': True},
        'state': {'readonly': True},
        'agent_jobs': {'readonly': True},
        'logins': {'readonly': True},
        'message': {'readonly': True},
        'server_role_results': {'readonly': True},
        'orphaned_users': {'readonly': True},
        'databases': {'readonly': True},
        'source_server_version': {'readonly': True},
        'source_server_brand_version': {'readonly': True},
        'target_server_version': {'readonly': True},
        'target_server_brand_version': {'readonly': True},
        'exceptions_and_warnings': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'agent_jobs': {'key': 'agentJobs', 'type': '{str}'},
        'logins': {'key': 'logins', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'server_role_results': {'key': 'serverRoleResults', 'type': '{StartMigrationScenarioServerRoleResult}'},
        'orphaned_users': {'key': 'orphanedUsers', 'type': '{str}'},
        'databases': {'key': 'databases', 'type': '{str}'},
        'source_server_version': {'key': 'sourceServerVersion', 'type': 'str'},
        'source_server_brand_version': {'key': 'sourceServerBrandVersion', 'type': 'str'},
        'target_server_version': {'key': 'targetServerVersion', 'type': 'str'},
        'target_server_brand_version': {'key': 'targetServerBrandVersion', 'type': 'str'},
        'exceptions_and_warnings': {'key': 'exceptionsAndWarnings', 'type': '[ReportableException]'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrateSqlServerSqlMITaskOutputMigrationLevel, self).__init__(**kwargs)
        self.started_on = None
        self.ended_on = None
        self.status = None
        self.state = None
        self.agent_jobs = None
        self.logins = None
        self.message = None
        self.server_role_results = None
        self.orphaned_users = None
        self.databases = None
        self.source_server_version = None
        self.source_server_brand_version = None
        self.target_server_version = None
        self.target_server_brand_version = None
        self.exceptions_and_warnings = None
        self.result_type = 'MigrationLevelOutput'
