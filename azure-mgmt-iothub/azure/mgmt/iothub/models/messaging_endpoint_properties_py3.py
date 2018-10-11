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


class MessagingEndpointProperties(Model):
    """The properties of the messaging endpoints used by this IoT hub.

    :param lock_duration_as_iso8601: The lock duration. See:
     https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-file-upload.
    :type lock_duration_as_iso8601: timedelta
    :param ttl_as_iso8601: The period of time for which a message is available
     to consume before it is expired by the IoT hub. See:
     https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-file-upload.
    :type ttl_as_iso8601: timedelta
    :param max_delivery_count: The number of times the IoT hub attempts to
     deliver a message. See:
     https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-file-upload.
    :type max_delivery_count: int
    """

    _validation = {
        'max_delivery_count': {'maximum': 100, 'minimum': 1},
    }

    _attribute_map = {
        'lock_duration_as_iso8601': {'key': 'lockDurationAsIso8601', 'type': 'duration'},
        'ttl_as_iso8601': {'key': 'ttlAsIso8601', 'type': 'duration'},
        'max_delivery_count': {'key': 'maxDeliveryCount', 'type': 'int'},
    }

    def __init__(self, *, lock_duration_as_iso8601=None, ttl_as_iso8601=None, max_delivery_count: int=None, **kwargs) -> None:
        super(MessagingEndpointProperties, self).__init__(**kwargs)
        self.lock_duration_as_iso8601 = lock_duration_as_iso8601
        self.ttl_as_iso8601 = ttl_as_iso8601
        self.max_delivery_count = max_delivery_count
