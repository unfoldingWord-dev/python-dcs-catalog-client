# dcs-catalog-client
This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.16.7+dcs
- Package version: 1.16.7
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import dcs_catalog_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dcs_catalog_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/catalog*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MiscApi* | [**misc_list_catalog_version_endpoints**](docs/MiscApi.md#misc_list_catalog_version_endpoints) | **GET** /misc/versions | Catalog Next version endpoint list, including what version \&quot;latest\&quot; points to
*V3Api* | [**catalog_search_v3**](docs/V3Api.md#catalog_search_v3) | **GET** /v3/search | Catalog v3 search
*V3Api* | [**catalog_subjects_pivoted_by_subject_v3**](docs/V3Api.md#catalog_subjects_pivoted_by_subject_v3) | **GET** /v3/subjects/{subject}.json | Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)
*V3Api* | [**catalog_subjects_pivoted_search_v3**](docs/V3Api.md#catalog_subjects_pivoted_search_v3) | **GET** /v3/subjects/search | Catalog v3 search pivoted by subject/language
*V3Api* | [**catalog_subjects_pivoted_v3**](docs/V3Api.md#catalog_subjects_pivoted_v3) | **GET** /v3/subjects/pivoted.json | Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json
*V3Api* | [**catalog_v3**](docs/V3Api.md#catalog_v3) | **GET** /v3/catalog.json | Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json
*V4Api* | [**catalo4_search_owner**](docs/V4Api.md#catalo4_search_owner) | **GET** /v4/search/{owner} | Catalog search by owner
*V4Api* | [**catalog_get_entry**](docs/V4Api.md#catalog_get_entry) | **GET** /v4/entry/{owner}/{repo}/{tag} | Catalog entry
*V4Api* | [**catalog_get_metadata**](docs/V4Api.md#catalog_get_metadata) | **GET** /v4/entry/{owner}/{repo}/{tag}/metadata | Catalog entry metadata (manifest.yaml in JSON format)
*V4Api* | [**catalog_search**](docs/V4Api.md#catalog_search) | **GET** /v4/search | Catalog search
*V4Api* | [**catalog_search_repo**](docs/V4Api.md#catalog_search_repo) | **GET** /v4/search/{owner}/{repo} | Catalog search by repo
*V5Api* | [**catalog_get_metadata**](docs/V5Api.md#catalog_get_metadata) | **GET** /v5/entry/{owner}/{repo}/{tag}/metadata | Catalog entry metadata (manifest.yaml in JSON format)
*V5Api* | [**catalog_search**](docs/V5Api.md#catalog_search) | **GET** /v5/search | Catalog search
*V5Api* | [**catalog_search_owner**](docs/V5Api.md#catalog_search_owner) | **GET** /v5/search/{owner} | Catalog search by owner
*V5Api* | [**catalog_search_repo**](docs/V5Api.md#catalog_search_repo) | **GET** /v5/search/{owner}/{repo} | Catalog search by repo
*V5Api* | [**catlog_get_entry**](docs/V5Api.md#catlog_get_entry) | **GET** /v5/entry/{owner}/{repo}/{tag} | Catalog entry


## Documentation For Models

 - [AccessToken](docs/AccessToken.md)
 - [Attachment](docs/Attachment.md)
 - [CatalogSearchResultsPivotedV3](docs/CatalogSearchResultsPivotedV3.md)
 - [CatalogSearchResultsV3](docs/CatalogSearchResultsV3.md)
 - [CatalogSearchResultsV4](docs/CatalogSearchResultsV4.md)
 - [CatalogSearchResultsV5](docs/CatalogSearchResultsV5.md)
 - [CatalogStage](docs/CatalogStage.md)
 - [CatalogStages](docs/CatalogStages.md)
 - [CatalogV3](docs/CatalogV3.md)
 - [CatalogV3Language](docs/CatalogV3Language.md)
 - [CatalogV3Pivoted](docs/CatalogV3Pivoted.md)
 - [CatalogV3Resource](docs/CatalogV3Resource.md)
 - [CatalogV3Subject](docs/CatalogV3Subject.md)
 - [CatalogV4](docs/CatalogV4.md)
 - [CatalogV5](docs/CatalogV5.md)
 - [CatalogVersionEndpoints](docs/CatalogVersionEndpoints.md)
 - [CatalogVersionEndpointsResponse](docs/CatalogVersionEndpointsResponse.md)
 - [ExternalTracker](docs/ExternalTracker.md)
 - [ExternalWiki](docs/ExternalWiki.md)
 - [InternalTracker](docs/InternalTracker.md)
 - [OAuth2Application](docs/OAuth2Application.md)
 - [Organization](docs/Organization.md)
 - [Permission](docs/Permission.md)
 - [Release](docs/Release.md)
 - [RepoTransfer](docs/RepoTransfer.md)
 - [Repository](docs/Repository.md)
 - [Team](docs/Team.md)
 - [User](docs/User.md)


## Documentation For Authorization


## AccessToken

- **Type**: API key
- **API key parameter name**: access_token
- **Location**: URL query string

## AuthorizationHeaderToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## BasicAuth

- **Type**: HTTP basic authentication

## SudoHeader

- **Type**: API key
- **API key parameter name**: Sudo
- **Location**: HTTP header

## SudoParam

- **Type**: API key
- **API key parameter name**: sudo
- **Location**: URL query string

## TOTPHeader

- **Type**: API key
- **API key parameter name**: X-GITEA-OTP
- **Location**: HTTP header

## Token

- **Type**: API key
- **API key parameter name**: token
- **Location**: URL query string


## Author



