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

from .answer import Answer


class SearchResultsAnswer(Answer):
    """SearchResultsAnswer.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: WebWebAnswer, Images, News,
    RelatedSearchesRelatedSearchAnswer, SpellSuggestions, TimeZone, Videos,
    Places

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries:
     list[~azure.cognitiveservices.search.websearch.models.Query]
    :ivar query_context:
    :vartype query_context:
     ~azure.cognitiveservices.search.websearch.models.QueryContext
    :ivar total_estimated_matches: The estimated number of webpages that are
     relevant to the query. Use this number along with the count and offset
     query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar is_family_friendly:
    :vartype is_family_friendly: bool
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
        'query_context': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'is_family_friendly': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
        'query_context': {'key': 'queryContext', 'type': 'QueryContext'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'is_family_friendly': {'key': 'isFamilyFriendly', 'type': 'bool'},
    }

    _subtype_map = {
        '_type': {'Web/WebAnswer': 'WebWebAnswer', 'Images': 'Images', 'News': 'News', 'RelatedSearches/RelatedSearchAnswer': 'RelatedSearchesRelatedSearchAnswer', 'SpellSuggestions': 'SpellSuggestions', 'TimeZone': 'TimeZone', 'Videos': 'Videos', 'Places': 'Places'}
    }

    def __init__(self, **kwargs):
        super(SearchResultsAnswer, self).__init__(**kwargs)
        self.query_context = None
        self.total_estimated_matches = None
        self.is_family_friendly = None
        self._type = 'SearchResultsAnswer'
