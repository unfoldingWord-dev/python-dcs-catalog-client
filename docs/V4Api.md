# dcs_catalog_client.V4Api

All URIs are relative to *http://localhost/api/catalog*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_search**](V4Api.md#catalog_search) | **GET** /v4/search | Catalog search
[**v4_get_catalog_entry**](V4Api.md#v4_get_catalog_entry) | **GET** /v4/entry/{owner}/{repo}/{tag} | Catalog entry
[**v4_get_metadata**](V4Api.md#v4_get_metadata) | **GET** /v4/entry/{owner}/{repo}/{tag}/metadata | Catalog entry metadata (manifest.yaml in JSON format)
[**v4_search_owner**](V4Api.md#v4_search_owner) | **GET** /v4/search/{owner} | Catalog search by owner
[**v4_search_repo**](V4Api.md#v4_search_repo) | **GET** /v4/search/{owner}/{repo} | Catalog search by repo


# **catalog_search**
> CatalogSearchResultsV4 catalog_search(q=q, owner=owner, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, checking_level=checking_level, book=book, include_history=include_history, include_metadata=include_metadata, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)

Catalog search

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
api_instance = dcs_catalog_client.V4Api(dcs_catalog_client.ApiClient(configuration))
q = 'q_example' # str | keyword(s). Can use multiple `q=<keyword>`s or commas for more than one keyword (optional)
owner = 'owner_example' # str | search only for entries with the given owner name(s). (optional)
repo = 'repo_example' # str | search only for entries with the given repo name(s). (optional)
tag = 'tag_example' # str | search only for entries with the given release tag(s) (optional)
lang = 'lang_example' # str | search only for entries with the given language(s) (optional)
stage = 'stage_example' # str | specifies which release stage to be return of these stages: \"prod\" - return only the production releases (default); \"preprod\" - return the pre-production release if it exists instead of the production release; \"draft\" - return the draft release if it exists instead of pre-production or production release; \"latest\" -return the default branch (e.g. master) if it is a valid RC instead of the above (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). Must match the entire string (case insensitive) (optional)
checking_level = 'checking_level_example' # str | search only for entries with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | search only for entries with the given book(s) (project ids) (optional)
include_history = true # bool | if true, all releases, not just the latest, are included. Default is false (optional)
include_metadata = true # bool | if false, only subject and title are searched with query terms, if true all metadata values are searched. Default is true (optional)
show_ingredients = true # bool | if true, a list of the projects in the resource and their file paths will be listed for each entry. Default is false (optional)
sort = 'sort_example' # str | sort repos alphanumerically by attribute. Supported values are \"subject\", \"title\", \"reponame\", \"tag\", \"released\", \"lang\", \"releases\", \"stars\", \"forks\". Default is by \"language\", \"subject\" and then \"tag\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, maximum page size is 50 (optional)

try:
    # Catalog search
    api_response = api_instance.catalog_search(q=q, owner=owner, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, checking_level=checking_level, book=book, include_history=include_history, include_metadata=include_metadata, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V4Api->catalog_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword(s). Can use multiple &#x60;q&#x3D;&lt;keyword&gt;&#x60;s or commas for more than one keyword | [optional] 
 **owner** | **str**| search only for entries with the given owner name(s). | [optional] 
 **repo** | **str**| search only for entries with the given repo name(s). | [optional] 
 **tag** | **str**| search only for entries with the given release tag(s) | [optional] 
 **lang** | **str**| search only for entries with the given language(s) | [optional] 
 **stage** | **str**| specifies which release stage to be return of these stages: \&quot;prod\&quot; - return only the production releases (default); \&quot;preprod\&quot; - return the pre-production release if it exists instead of the production release; \&quot;draft\&quot; - return the draft release if it exists instead of pre-production or production release; \&quot;latest\&quot; -return the default branch (e.g. master) if it is a valid RC instead of the above | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). Must match the entire string (case insensitive) | [optional] 
 **checking_level** | **str**| search only for entries with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| search only for entries with the given book(s) (project ids) | [optional] 
 **include_history** | **bool**| if true, all releases, not just the latest, are included. Default is false | [optional] 
 **include_metadata** | **bool**| if false, only subject and title are searched with query terms, if true all metadata values are searched. Default is true | [optional] 
 **show_ingredients** | **bool**| if true, a list of the projects in the resource and their file paths will be listed for each entry. Default is false | [optional] 
 **sort** | **str**| sort repos alphanumerically by attribute. Supported values are \&quot;subject\&quot;, \&quot;title\&quot;, \&quot;reponame\&quot;, \&quot;tag\&quot;, \&quot;released\&quot;, \&quot;lang\&quot;, \&quot;releases\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot;. Default is by \&quot;language\&quot;, \&quot;subject\&quot; and then \&quot;tag\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, maximum page size is 50 | [optional] 

### Return type

[**CatalogSearchResultsV4**](CatalogSearchResultsV4.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_get_catalog_entry**
> CatalogV4 v4_get_catalog_entry(owner, repo, tag)

Catalog entry

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
api_instance = dcs_catalog_client.V4Api(dcs_catalog_client.ApiClient(configuration))
owner = 'owner_example' # str | name of the owner
repo = 'repo_example' # str | name of the repo
tag = 'tag_example' # str | release tag or default branch

try:
    # Catalog entry
    api_response = api_instance.v4_get_catalog_entry(owner, repo, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V4Api->v4_get_catalog_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repo | 
 **tag** | **str**| release tag or default branch | 

### Return type

[**CatalogV4**](CatalogV4.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_get_metadata**
> dict(str, object) v4_get_metadata(owner, repo, tag)

Catalog entry metadata (manifest.yaml in JSON format)

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
api_instance = dcs_catalog_client.V4Api(dcs_catalog_client.ApiClient(configuration))
owner = 'owner_example' # str | name of the owner
repo = 'repo_example' # str | name of the repo
tag = 'tag_example' # str | release tag or default branch

try:
    # Catalog entry metadata (manifest.yaml in JSON format)
    api_response = api_instance.v4_get_metadata(owner, repo, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V4Api->v4_get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repo | 
 **tag** | **str**| release tag or default branch | 

### Return type

**dict(str, object)**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_search_owner**
> CatalogSearchResultsV4 v4_search_owner(owner, q=q, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, checking_level=checking_level, book=book, include_history=include_history, include_metadata=include_metadata, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)

Catalog search by owner

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
api_instance = dcs_catalog_client.V4Api(dcs_catalog_client.ApiClient(configuration))
owner = 'owner_example' # str | owner of entries
q = 'q_example' # str | keyword(s). Can use multiple `q=<keyword>`s or commas for more than one keyword (optional)
repo = 'repo_example' # str | search only for entries with the given repo name(s). (optional)
tag = 'tag_example' # str | search only for entries with the given release tag(s) (optional)
lang = 'lang_example' # str | search only for entries with the given language(s) (optional)
stage = 'stage_example' # str | specifies which release stage to be return of these stages: \"prod\" - return only the production releases (default); \"preprod\" - return the pre-production release if it exists instead of the production release; \"draft\" - return the draft release if it exists instead of pre-production or production release; \"latest\" -return the default branch (e.g. master) if it is a valid RC instead of the above (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). Must match the entire string (case insensitive) (optional)
checking_level = 'checking_level_example' # str | search only for entries with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | search only for entries with the given book(s) (project ids) (optional)
include_history = true # bool | if true, all releases, not just the latest, are included. Default is false (optional)
include_metadata = true # bool | if false, only subject and title are searched with query terms, if true all metadata values are searched. Default is true (optional)
show_ingredients = true # bool | if true, a list of the projects in the resource and their file paths will be listed for each entry. Default is false (optional)
sort = 'sort_example' # str | sort repos alphanumerically by attribute. Supported values are \"subject\", \"title\", \"reponame\", \"tag\", \"released\", \"lang\", \"releases\", \"stars\", \"forks\". Default is by \"language\", \"subject\" and then \"tag\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, maximum page size is 50 (optional)

try:
    # Catalog search by owner
    api_response = api_instance.v4_search_owner(owner, q=q, repo=repo, tag=tag, lang=lang, stage=stage, subject=subject, checking_level=checking_level, book=book, include_history=include_history, include_metadata=include_metadata, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V4Api->v4_search_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of entries | 
 **q** | **str**| keyword(s). Can use multiple &#x60;q&#x3D;&lt;keyword&gt;&#x60;s or commas for more than one keyword | [optional] 
 **repo** | **str**| search only for entries with the given repo name(s). | [optional] 
 **tag** | **str**| search only for entries with the given release tag(s) | [optional] 
 **lang** | **str**| search only for entries with the given language(s) | [optional] 
 **stage** | **str**| specifies which release stage to be return of these stages: \&quot;prod\&quot; - return only the production releases (default); \&quot;preprod\&quot; - return the pre-production release if it exists instead of the production release; \&quot;draft\&quot; - return the draft release if it exists instead of pre-production or production release; \&quot;latest\&quot; -return the default branch (e.g. master) if it is a valid RC instead of the above | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). Must match the entire string (case insensitive) | [optional] 
 **checking_level** | **str**| search only for entries with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| search only for entries with the given book(s) (project ids) | [optional] 
 **include_history** | **bool**| if true, all releases, not just the latest, are included. Default is false | [optional] 
 **include_metadata** | **bool**| if false, only subject and title are searched with query terms, if true all metadata values are searched. Default is true | [optional] 
 **show_ingredients** | **bool**| if true, a list of the projects in the resource and their file paths will be listed for each entry. Default is false | [optional] 
 **sort** | **str**| sort repos alphanumerically by attribute. Supported values are \&quot;subject\&quot;, \&quot;title\&quot;, \&quot;reponame\&quot;, \&quot;tag\&quot;, \&quot;released\&quot;, \&quot;lang\&quot;, \&quot;releases\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot;. Default is by \&quot;language\&quot;, \&quot;subject\&quot; and then \&quot;tag\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, maximum page size is 50 | [optional] 

### Return type

[**CatalogSearchResultsV4**](CatalogSearchResultsV4.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_search_repo**
> CatalogSearchResultsV4 v4_search_repo(owner, repo, q=q, tag=tag, lang=lang, stage=stage, subject=subject, checking_level=checking_level, book=book, include_history=include_history, include_metadata=include_metadata, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)

Catalog search by repo

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
api_instance = dcs_catalog_client.V4Api(dcs_catalog_client.ApiClient(configuration))
owner = 'owner_example' # str | name of the owner
repo = 'repo_example' # str | name of the repo
q = 'q_example' # str | keyword(s). Can use multiple `q=<keyword>`s or commas for more than one keyword (optional)
tag = 'tag_example' # str | search only for entries with the given release tag(s) (optional)
lang = 'lang_example' # str | search only for entries with the given language(s) (optional)
stage = 'stage_example' # str | specifies which release stage to be return of these stages: \"prod\" - return only the production releases (default); \"preprod\" - return the pre-production release if it exists instead of the production release; \"draft\" - return the draft release if it exists instead of pre-production or production release; \"latest\" -return the default branch (e.g. master) if it is a valid RC instead of the above (optional)
subject = 'subject_example' # str | search only for entries with the given subject(s). Must match the entire string (case insensitive) (optional)
checking_level = 'checking_level_example' # str | search only for entries with the given checking level(s). Can be 1, 2 or 3 (optional)
book = 'book_example' # str | search only for entries with the given book(s) (project ids) (optional)
include_history = true # bool | if true, all releases, not just the latest, are included. Default is false (optional)
include_metadata = true # bool | if false, only subject and title are searched with query terms, if true all metadata values are searched. Default is true (optional)
show_ingredients = true # bool | if true, a list of the projects in the resource and their file paths will be listed for each entry. Default is false (optional)
sort = 'sort_example' # str | sort repos alphanumerically by attribute. Supported values are \"subject\", \"title\", \"reponame\", \"tag\", \"released\", \"lang\", \"releases\", \"stars\", \"forks\". Default is by \"language\", \"subject\" and then \"tag\" (optional)
order = 'order_example' # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
page = 56 # int | page number of results to return (1-based) (optional)
limit = 56 # int | page size of results, maximum page size is 50 (optional)

try:
    # Catalog search by repo
    api_response = api_instance.v4_search_repo(owner, repo, q=q, tag=tag, lang=lang, stage=stage, subject=subject, checking_level=checking_level, book=book, include_history=include_history, include_metadata=include_metadata, show_ingredients=show_ingredients, sort=sort, order=order, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V4Api->v4_search_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| name of the owner | 
 **repo** | **str**| name of the repo | 
 **q** | **str**| keyword(s). Can use multiple &#x60;q&#x3D;&lt;keyword&gt;&#x60;s or commas for more than one keyword | [optional] 
 **tag** | **str**| search only for entries with the given release tag(s) | [optional] 
 **lang** | **str**| search only for entries with the given language(s) | [optional] 
 **stage** | **str**| specifies which release stage to be return of these stages: \&quot;prod\&quot; - return only the production releases (default); \&quot;preprod\&quot; - return the pre-production release if it exists instead of the production release; \&quot;draft\&quot; - return the draft release if it exists instead of pre-production or production release; \&quot;latest\&quot; -return the default branch (e.g. master) if it is a valid RC instead of the above | [optional] 
 **subject** | **str**| search only for entries with the given subject(s). Must match the entire string (case insensitive) | [optional] 
 **checking_level** | **str**| search only for entries with the given checking level(s). Can be 1, 2 or 3 | [optional] 
 **book** | **str**| search only for entries with the given book(s) (project ids) | [optional] 
 **include_history** | **bool**| if true, all releases, not just the latest, are included. Default is false | [optional] 
 **include_metadata** | **bool**| if false, only subject and title are searched with query terms, if true all metadata values are searched. Default is true | [optional] 
 **show_ingredients** | **bool**| if true, a list of the projects in the resource and their file paths will be listed for each entry. Default is false | [optional] 
 **sort** | **str**| sort repos alphanumerically by attribute. Supported values are \&quot;subject\&quot;, \&quot;title\&quot;, \&quot;reponame\&quot;, \&quot;tag\&quot;, \&quot;released\&quot;, \&quot;lang\&quot;, \&quot;releases\&quot;, \&quot;stars\&quot;, \&quot;forks\&quot;. Default is by \&quot;language\&quot;, \&quot;subject\&quot; and then \&quot;tag\&quot; | [optional] 
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results, maximum page size is 50 | [optional] 

### Return type

[**CatalogSearchResultsV4**](CatalogSearchResultsV4.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

