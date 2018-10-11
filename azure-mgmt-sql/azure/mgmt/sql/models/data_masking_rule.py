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

from .proxy_resource import ProxyResource


class DataMaskingRule(ProxyResource):
    """Represents a database data masking rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar data_masking_rule_id: The rule Id.
    :vartype data_masking_rule_id: str
    :param alias_name: The alias name. This is a legacy parameter and is no
     longer used.
    :type alias_name: str
    :param rule_state: The rule state. Used to delete a rule. To delete an
     existing rule, specify the schemaName, tableName, columnName,
     maskingFunction, and specify ruleState as disabled. However, if the rule
     doesn't already exist, the rule will be created with ruleState set to
     enabled, regardless of the provided value of ruleState. Possible values
     include: 'Disabled', 'Enabled'
    :type rule_state: str or ~azure.mgmt.sql.models.DataMaskingRuleState
    :param schema_name: Required. The schema name on which the data masking
     rule is applied.
    :type schema_name: str
    :param table_name: Required. The table name on which the data masking rule
     is applied.
    :type table_name: str
    :param column_name: Required. The column name on which the data masking
     rule is applied.
    :type column_name: str
    :param masking_function: Required. The masking function that is used for
     the data masking rule. Possible values include: 'Default', 'CCN', 'Email',
     'Number', 'SSN', 'Text'
    :type masking_function: str or ~azure.mgmt.sql.models.DataMaskingFunction
    :param number_from: The numberFrom property of the masking rule. Required
     if maskingFunction is set to Number, otherwise this parameter will be
     ignored.
    :type number_from: str
    :param number_to: The numberTo property of the data masking rule. Required
     if maskingFunction is set to Number, otherwise this parameter will be
     ignored.
    :type number_to: str
    :param prefix_size: If maskingFunction is set to Text, the number of
     characters to show unmasked in the beginning of the string. Otherwise,
     this parameter will be ignored.
    :type prefix_size: str
    :param suffix_size: If maskingFunction is set to Text, the number of
     characters to show unmasked at the end of the string. Otherwise, this
     parameter will be ignored.
    :type suffix_size: str
    :param replacement_string: If maskingFunction is set to Text, the
     character to use for masking the unexposed part of the string. Otherwise,
     this parameter will be ignored.
    :type replacement_string: str
    :ivar location: The location of the data masking rule.
    :vartype location: str
    :ivar kind: The kind of Data Masking Rule. Metadata, used for Azure
     portal.
    :vartype kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'data_masking_rule_id': {'readonly': True},
        'schema_name': {'required': True},
        'table_name': {'required': True},
        'column_name': {'required': True},
        'masking_function': {'required': True},
        'location': {'readonly': True},
        'kind': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'data_masking_rule_id': {'key': 'properties.id', 'type': 'str'},
        'alias_name': {'key': 'properties.aliasName', 'type': 'str'},
        'rule_state': {'key': 'properties.ruleState', 'type': 'DataMaskingRuleState'},
        'schema_name': {'key': 'properties.schemaName', 'type': 'str'},
        'table_name': {'key': 'properties.tableName', 'type': 'str'},
        'column_name': {'key': 'properties.columnName', 'type': 'str'},
        'masking_function': {'key': 'properties.maskingFunction', 'type': 'DataMaskingFunction'},
        'number_from': {'key': 'properties.numberFrom', 'type': 'str'},
        'number_to': {'key': 'properties.numberTo', 'type': 'str'},
        'prefix_size': {'key': 'properties.prefixSize', 'type': 'str'},
        'suffix_size': {'key': 'properties.suffixSize', 'type': 'str'},
        'replacement_string': {'key': 'properties.replacementString', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataMaskingRule, self).__init__(**kwargs)
        self.data_masking_rule_id = None
        self.alias_name = kwargs.get('alias_name', None)
        self.rule_state = kwargs.get('rule_state', None)
        self.schema_name = kwargs.get('schema_name', None)
        self.table_name = kwargs.get('table_name', None)
        self.column_name = kwargs.get('column_name', None)
        self.masking_function = kwargs.get('masking_function', None)
        self.number_from = kwargs.get('number_from', None)
        self.number_to = kwargs.get('number_to', None)
        self.prefix_size = kwargs.get('prefix_size', None)
        self.suffix_size = kwargs.get('suffix_size', None)
        self.replacement_string = kwargs.get('replacement_string', None)
        self.location = None
        self.kind = None
