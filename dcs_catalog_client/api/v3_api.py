# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 1.16.7+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dcs_catalog_client.api_client import ApiClient


class V3Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def catalog_search_v3(self, **kwargs):  # noqa: E501
        """Catalog v3 search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_search_v3(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str repo: search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str lang: search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive)
        :param str subject: search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param bool partial_match: if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false
        :return: CatalogSearchResultsV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalog_search_v3_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.catalog_search_v3_with_http_info(**kwargs)  # noqa: E501
            return data

    def catalog_search_v3_with_http_info(self, **kwargs):  # noqa: E501
        """Catalog v3 search  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_search_v3_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str repo: search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str lang: search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive)
        :param str subject: search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param bool partial_match: if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false
        :return: CatalogSearchResultsV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'lang', 'subject', 'partial_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_search_v3" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'subject' in params:
            query_params.append(('subject', params['subject']))  # noqa: E501
        if 'partial_match' in params:
            query_params.append(('partialMatch', params['partial_match']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/v3/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogSearchResultsV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalog_subjects_pivoted_by_subject_v3(self, subject, **kwargs):  # noqa: E501
        """Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_subjects_pivoted_by_subject_v3(subject, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subject: subject to query (required)
        :return: CatalogSearchResultsPivotedV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalog_subjects_pivoted_by_subject_v3_with_http_info(subject, **kwargs)  # noqa: E501
        else:
            (data) = self.catalog_subjects_pivoted_by_subject_v3_with_http_info(subject, **kwargs)  # noqa: E501
            return data

    def catalog_subjects_pivoted_by_subject_v3_with_http_info(self, subject, **kwargs):  # noqa: E501
        """Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_subjects_pivoted_by_subject_v3_with_http_info(subject, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str subject: subject to query (required)
        :return: CatalogSearchResultsPivotedV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subject']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_subjects_pivoted_by_subject_v3" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subject' is set
        if self.api_client.client_side_validation and ('subject' not in params or
                                                       params['subject'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `subject` when calling `catalog_subjects_pivoted_by_subject_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'subject' in params:
            path_params['subject'] = params['subject']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/v3/subjects/{subject}.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogSearchResultsPivotedV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalog_subjects_pivoted_search_v3(self, **kwargs):  # noqa: E501
        """Catalog v3 search pivoted by subject/language  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_subjects_pivoted_search_v3(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str repo: search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str lang: search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive)
        :param str subject: search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param bool partial_match: if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false
        :return: CatalogSearchResultsPivotedV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalog_subjects_pivoted_search_v3_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.catalog_subjects_pivoted_search_v3_with_http_info(**kwargs)  # noqa: E501
            return data

    def catalog_subjects_pivoted_search_v3_with_http_info(self, **kwargs):  # noqa: E501
        """Catalog v3 search pivoted by subject/language  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_subjects_pivoted_search_v3_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner: search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str repo: search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param str lang: search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive)
        :param str subject: search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true
        :param bool partial_match: if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false
        :return: CatalogSearchResultsPivotedV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'repo', 'lang', 'subject', 'partial_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_subjects_pivoted_search_v3" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501
        if 'repo' in params:
            query_params.append(('repo', params['repo']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'subject' in params:
            query_params.append(('subject', params['subject']))  # noqa: E501
        if 'partial_match' in params:
            query_params.append(('partialMatch', params['partial_match']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/v3/subjects/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogSearchResultsPivotedV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalog_subjects_pivoted_v3(self, **kwargs):  # noqa: E501
        """Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_subjects_pivoted_v3(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CatalogSearchResultsPivotedV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalog_subjects_pivoted_v3_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.catalog_subjects_pivoted_v3_with_http_info(**kwargs)  # noqa: E501
            return data

    def catalog_subjects_pivoted_v3_with_http_info(self, **kwargs):  # noqa: E501
        """Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_subjects_pivoted_v3_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CatalogSearchResultsPivotedV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_subjects_pivoted_v3" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/v3/subjects/pivoted.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogSearchResultsPivotedV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalog_v3(self, **kwargs):  # noqa: E501
        """Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_v3(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CatalogSearchResultsV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalog_v3_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.catalog_v3_with_http_info(**kwargs)  # noqa: E501
            return data

    def catalog_v3_with_http_info(self, **kwargs):  # noqa: E501
        """Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalog_v3_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CatalogSearchResultsV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_v3" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['AccessToken', 'AuthorizationHeaderToken', 'BasicAuth', 'SudoHeader', 'SudoParam', 'TOTPHeader', 'Token']  # noqa: E501

        return self.api_client.call_api(
            '/v3/catalog.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CatalogSearchResultsV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
