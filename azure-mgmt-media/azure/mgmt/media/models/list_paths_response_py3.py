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


class ListPathsResponse(Model):
    """Class of response for listPaths action.

    :param streaming_paths: Streaming Paths supported by current Streaming
     Locator
    :type streaming_paths: list[~azure.mgmt.media.models.StreamingPath]
    :param download_paths: Download Paths supported by current Streaming
     Locator
    :type download_paths: list[str]
    """

    _attribute_map = {
        'streaming_paths': {'key': 'streamingPaths', 'type': '[StreamingPath]'},
        'download_paths': {'key': 'downloadPaths', 'type': '[str]'},
    }

    def __init__(self, *, streaming_paths=None, download_paths=None, **kwargs) -> None:
        super(ListPathsResponse, self).__init__(**kwargs)
        self.streaming_paths = streaming_paths
        self.download_paths = download_paths
