# dcs_catalog_client.V3Api

All URIs are relative to *http://localhost/api/catalog*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_search_v3**](V3Api.md#catalog_search_v3) | **GET** /v3/search | Catalog v3 search
[**catalog_subjects_pivoted_by_subject_v3**](V3Api.md#catalog_subjects_pivoted_by_subject_v3) | **GET** /v3/subjects/{subject}.json | Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)
[**catalog_subjects_pivoted_search_v3**](V3Api.md#catalog_subjects_pivoted_search_v3) | **GET** /v3/subjects/search | Catalog v3 search pivoted by subject/language
[**catalog_subjects_pivoted_v3**](V3Api.md#catalog_subjects_pivoted_v3) | **GET** /v3/subjects/pivoted.json | Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json
[**catalog_v3**](V3Api.md#catalog_v3) | **GET** /v3/catalog.json | Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json


# **catalog_search_v3**
> CatalogSearchResultsV3 catalog_search_v3(owner=owner, repo=repo, lang=lang, subject=subject, partial_match=partial_match)

Catalog v3 search

### Example
```python
from __future__ import print_function
import time
import dcs_catalog_client
from dcs_catalog_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_catalog_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_catalog_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_catalog_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_catalog_client.V3Api(dcs_catalog_client.ApiClient(configuration))
owner = 'owner_example' # str | search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
repo = 'repo_example' # str | search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
lang = 'lang_example' # str | search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
partial_match = true # bool | if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)

try:
    # Catalog v3 search
    api_response = api_instance.catalog_search_v3(owner=owner, repo=repo, lang=lang, subject=subject, partial_match=partial_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3Api->catalog_search_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **repo** | **str**| search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **lang** | **str**| search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **partial_match** | **bool**| if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 

### Return type

[**CatalogSearchResultsV3**](CatalogSearchResultsV3.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_subjects_pivoted_by_subject_v3**
> CatalogSearchResultsPivotedV3 catalog_subjects_pivoted_by_subject_v3(subject)

Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)

### Example
```python
from __future__ import print_function
import time
import dcs_catalog_client
from dcs_catalog_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_catalog_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_catalog_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_catalog_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_catalog_client.V3Api(dcs_catalog_client.ApiClient(configuration))
subject = 'subject_example' # str | subject to query

try:
    # Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)
    api_response = api_instance.catalog_subjects_pivoted_by_subject_v3(subject)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3Api->catalog_subjects_pivoted_by_subject_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| subject to query | 

### Return type

[**CatalogSearchResultsPivotedV3**](CatalogSearchResultsPivotedV3.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_subjects_pivoted_search_v3**
> CatalogSearchResultsPivotedV3 catalog_subjects_pivoted_search_v3(owner=owner, repo=repo, lang=lang, subject=subject, partial_match=partial_match)

Catalog v3 search pivoted by subject/language

### Example
```python
from __future__ import print_function
import time
import dcs_catalog_client
from dcs_catalog_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_catalog_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_catalog_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_catalog_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_catalog_client.V3Api(dcs_catalog_client.ApiClient(configuration))
owner = 'owner_example' # str | search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
repo = 'repo_example' # str | search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
lang = 'lang_example' # str | search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch=true (optional)
partial_match = true # bool | if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false (optional)

try:
    # Catalog v3 search pivoted by subject/language
    api_response = api_instance.catalog_subjects_pivoted_search_v3(owner=owner, repo=repo, lang=lang, subject=subject, partial_match=partial_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3Api->catalog_subjects_pivoted_search_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| search only for entries with the given owner name(s). Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **repo** | **str**| search only for entries with the given repo name(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **lang** | **str**| search only for entries with the given language(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). To match multiple, give the parameter multiple times or give a list comma delimited. Will perform an exact match (case insensitive) unlesss partialMatch&#x3D;true | [optional] 
 **partial_match** | **bool**| if true, subject, owner and repo search fields will use partial match (LIKE) when querying the catalog. Default is false | [optional] 

### Return type

[**CatalogSearchResultsPivotedV3**](CatalogSearchResultsPivotedV3.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_subjects_pivoted_v3**
> CatalogSearchResultsPivotedV3 catalog_subjects_pivoted_v3()

Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json

### Example
```python
from __future__ import print_function
import time
import dcs_catalog_client
from dcs_catalog_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_catalog_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_catalog_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_catalog_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_catalog_client.V3Api(dcs_catalog_client.ApiClient(configuration))

try:
    # Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json
    api_response = api_instance.catalog_subjects_pivoted_v3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3Api->catalog_subjects_pivoted_v3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogSearchResultsPivotedV3**](CatalogSearchResultsPivotedV3.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_v3**
> CatalogSearchResultsV3 catalog_v3()

Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json

### Example
```python
from __future__ import print_function
import time
import dcs_catalog_client
from dcs_catalog_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: AccessToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['access_token'] = 'Bearer'
# Configure API key authorization: AuthorizationHeaderToken
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: BasicAuth
configuration = dcs_catalog_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: SudoHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['Sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Sudo'] = 'Bearer'
# Configure API key authorization: SudoParam
configuration = dcs_catalog_client.Configuration()
configuration.api_key['sudo'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sudo'] = 'Bearer'
# Configure API key authorization: TOTPHeader
configuration = dcs_catalog_client.Configuration()
configuration.api_key['X-GITEA-OTP'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GITEA-OTP'] = 'Bearer'
# Configure API key authorization: Token
configuration = dcs_catalog_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = dcs_catalog_client.V3Api(dcs_catalog_client.ApiClient(configuration))

try:
    # Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json
    api_response = api_instance.catalog_v3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V3Api->catalog_v3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogSearchResultsV3**](CatalogSearchResultsV3.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

