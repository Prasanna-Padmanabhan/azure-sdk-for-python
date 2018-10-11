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


class MigrationReportResult(Model):
    """Migration validation report result, contains the url for downloading the
    generated report.

    :param id: Migration validation result identifier
    :type id: str
    :param report_url: The url of the report.
    :type report_url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'report_url': {'key': 'reportUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MigrationReportResult, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.report_url = kwargs.get('report_url', None)
