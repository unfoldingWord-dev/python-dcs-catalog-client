# dcs_catalog_client.MiscApi

All URIs are relative to *http://localhost/api/catalog*

Method | HTTP request | Description
------------- | ------------- | -------------
[**misc_list_catalog_version_endpoints**](MiscApi.md#misc_list_catalog_version_endpoints) | **GET** /misc/versions | Catalog Next version endpoint list, including what version \&quot;latest\&quot; points to


# **misc_list_catalog_version_endpoints**
> CatalogVersionEndpointsResponse misc_list_catalog_version_endpoints()

Catalog Next version endpoint list, including what version \"latest\" points to

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
api_instance = dcs_catalog_client.MiscApi(dcs_catalog_client.ApiClient(configuration))

try:
    # Catalog Next version endpoint list, including what version \"latest\" points to
    api_response = api_instance.misc_list_catalog_version_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->misc_list_catalog_version_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogVersionEndpointsResponse**](CatalogVersionEndpointsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

