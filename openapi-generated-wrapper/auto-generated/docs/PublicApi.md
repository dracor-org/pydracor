# openapi_client.PublicApi

All URIs are relative to *https://dracor.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_info**](PublicApi.md#api_info) | **GET** /info | API info
[**corpus_metadata**](PublicApi.md#corpus_metadata) | **GET** /corpora/{corpusname}/metadata | List of metadata for all plays in a corpus
[**corpus_metadata_csv_endpoint**](PublicApi.md#corpus_metadata_csv_endpoint) | **GET** /corpora/{corpusname}/metadata/csv | List of metadata for all plays in a corpus
[**get_characters**](PublicApi.md#get_characters) | **GET** /corpora/{corpusname}/plays/{playname}/characters | Get a list of characters of a play
[**get_characters_csv**](PublicApi.md#get_characters_csv) | **GET** /corpora/{corpusname}/plays/{playname}/characters/csv | Get a list of characters of a play (CSV)
[**list_corpora**](PublicApi.md#list_corpora) | **GET** /corpora | List available corpora
[**list_corpus_content**](PublicApi.md#list_corpus_content) | **GET** /corpora/{corpusname} | List corpus content
[**network_csv**](PublicApi.md#network_csv) | **GET** /corpora/{corpusname}/plays/{playname}/networkdata/csv | Get network data of a play as CSV
[**network_gexf**](PublicApi.md#network_gexf) | **GET** /corpora/{corpusname}/plays/{playname}/networkdata/gexf | Get network data of a play as GEXF
[**network_graphml**](PublicApi.md#network_graphml) | **GET** /corpora/{corpusname}/plays/{playname}/networkdata/graphml | Get network data of a play as GraphML
[**play_info**](PublicApi.md#play_info) | **GET** /corpora/{corpusname}/plays/{playname} | Get metadata and network metrics for a single play
[**play_metrics**](PublicApi.md#play_metrics) | **GET** /corpora/{corpusname}/plays/{playname}/metrics | Get network metrics for a single play
[**play_spoken_text**](PublicApi.md#play_spoken_text) | **GET** /corpora/{corpusname}/plays/{playname}/spoken-text | Get spoken text of a play (excluding stage directions)
[**play_spoken_text_by_character**](PublicApi.md#play_spoken_text_by_character) | **GET** /corpora/{corpusname}/plays/{playname}/spoken-text-by-character | Get spoken text for each character of a play
[**play_stage_directions**](PublicApi.md#play_stage_directions) | **GET** /corpora/{corpusname}/plays/{playname}/stage-directions | Get all stage directions of a play
[**play_stage_directions_with_speakers**](PublicApi.md#play_stage_directions_with_speakers) | **GET** /corpora/{corpusname}/plays/{playname}/stage-directions-with-speakers | Get all stage directions of a play including speakers
[**play_tei**](PublicApi.md#play_tei) | **GET** /corpora/{corpusname}/plays/{playname}/tei | Get TEI document of a single play
[**plays_with_character**](PublicApi.md#plays_with_character) | **GET** /character/{id} | List plays having a character identified by Wikidata ID
[**relations_csv**](PublicApi.md#relations_csv) | **GET** /corpora/{corpusname}/plays/{playname}/relations/csv | Get relation data of a play as CSV
[**relations_gexf**](PublicApi.md#relations_gexf) | **GET** /corpora/{corpusname}/plays/{playname}/relations/gexf | Get relation data of a play as GEXF
[**relations_graphml**](PublicApi.md#relations_graphml) | **GET** /corpora/{corpusname}/plays/{playname}/relations/graphml | Get relation data of a play as GraphML
[**resolve_id**](PublicApi.md#resolve_id) | **GET** /id/{id} | Resolve DraCor play ID


# **api_info**
> Info api_info()

API info

Shows version numbers of the dracor-api app and the underlying eXist-db.

### Example


```python
import openapi_client
from openapi_client.models.info import Info
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)

    try:
        # API info
        api_response = api_instance.api_info()
        print("The response of PublicApi->api_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->api_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Info**](Info.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns JSON object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corpus_metadata**
> List[PlayMetadata] corpus_metadata(corpusname)

List of metadata for all plays in a corpus

### Example


```python
import openapi_client
from openapi_client.models.play_metadata import PlayMetadata
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 

    try:
        # List of metadata for all plays in a corpus
        api_response = api_instance.corpus_metadata(corpusname)
        print("The response of PublicApi->corpus_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->corpus_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 

### Return type

[**List[PlayMetadata]**](PlayMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of metadata for all plays |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corpus_metadata_csv_endpoint**
> str corpus_metadata_csv_endpoint(corpusname)

List of metadata for all plays in a corpus

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 

    try:
        # List of metadata for all plays in a corpus
        api_response = api_instance.corpus_metadata_csv_endpoint(corpusname)
        print("The response of PublicApi->corpus_metadata_csv_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->corpus_metadata_csv_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a comma separated list of metadata for all plays |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters**
> List[Character] get_characters(corpusname, playname)

Get a list of characters of a play

### Example


```python
import openapi_client
from openapi_client.models.character import Character
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get a list of characters of a play
        api_response = api_instance.get_characters(corpusname, playname)
        print("The response of PublicApi->get_characters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_characters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

[**List[Character]**](Character.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of characters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_csv**
> str get_characters_csv(corpusname, playname)

Get a list of characters of a play (CSV)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get a list of characters of a play (CSV)
        api_response = api_instance.get_characters_csv(corpusname, playname)
        print("The response of PublicApi->get_characters_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_characters_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of characters as CSV |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_corpora**
> List[CorpusInCorpora] list_corpora(include=include)

List available corpora

### Example


```python
import openapi_client
from openapi_client.models.corpus_in_corpora import CorpusInCorpora
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    include = 'include_example' # str | Include metrics for each corpus (optional)

    try:
        # List available corpora
        api_response = api_instance.list_corpora(include=include)
        print("The response of PublicApi->list_corpora:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->list_corpora: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Include metrics for each corpus | [optional] 

### Return type

[**List[CorpusInCorpora]**](CorpusInCorpora.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns list of available corpora |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_corpus_content**
> Corpus list_corpus_content(corpusname)

List corpus content

Lists all plays available in the corpus including the id, title, author(s) and other meta data.

### Example


```python
import openapi_client
from openapi_client.models.corpus import Corpus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 

    try:
        # List corpus content
        api_response = api_instance.list_corpus_content(corpusname)
        print("The response of PublicApi->list_corpus_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->list_corpus_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 

### Return type

[**Corpus**](Corpus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns object representing corpus contents |  -  |
**404** | Corpus not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_csv**
> str network_csv(corpusname, playname)

Get network data of a play as CSV

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get network data of a play as CSV
        api_response = api_instance.network_csv(corpusname, playname)
        print("The response of PublicApi->network_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->network_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns CSV file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_gexf**
> str network_gexf(corpusname, playname)

Get network data of a play as GEXF

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get network data of a play as GEXF
        api_response = api_instance.network_gexf(corpusname, playname)
        print("The response of PublicApi->network_gexf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->network_gexf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns GEXF file. See [Specification](https://gexf.net). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_graphml**
> str network_graphml(corpusname, playname)

Get network data of a play as GraphML

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get network data of a play as GraphML
        api_response = api_instance.network_graphml(corpusname, playname)
        print("The response of PublicApi->network_graphml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->network_graphml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns GraphML file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_info**
> Play play_info(corpusname, playname)

Get metadata and network metrics for a single play

### Example


```python
import openapi_client
from openapi_client.models.play import Play
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get metadata and network metrics for a single play
        api_response = api_instance.play_info(corpusname, playname)
        print("The response of PublicApi->play_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

[**Play**](Play.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an object with play meta data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_metrics**
> PlayMetrics play_metrics(corpusname, playname)

Get network metrics for a single play

### Example


```python
import openapi_client
from openapi_client.models.play_metrics import PlayMetrics
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get network metrics for a single play
        api_response = api_instance.play_metrics(corpusname, playname)
        print("The response of PublicApi->play_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

[**PlayMetrics**](PlayMetrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an object with metrics data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_spoken_text**
> str play_spoken_text(corpusname, playname, gender=gender, relation=relation, role=role)

Get spoken text of a play (excluding stage directions)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 
    gender = 'gender_example' # str |  (optional)
    relation = 'relation_example' # str |  (optional)
    role = 'role_example' # str |  (optional)

    try:
        # Get spoken text of a play (excluding stage directions)
        api_response = api_instance.play_spoken_text(corpusname, playname, gender=gender, relation=relation, role=role)
        print("The response of PublicApi->play_spoken_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_spoken_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 
 **gender** | **str**|  | [optional] 
 **relation** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns plain text document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_spoken_text_by_character**
> List[SpokenTextByCharacter] play_spoken_text_by_character(corpusname, playname)

Get spoken text for each character of a play

### Example


```python
import openapi_client
from openapi_client.models.spoken_text_by_character import SpokenTextByCharacter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get spoken text for each character of a play
        api_response = api_instance.play_spoken_text_by_character(corpusname, playname)
        print("The response of PublicApi->play_spoken_text_by_character:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_spoken_text_by_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

[**List[SpokenTextByCharacter]**](SpokenTextByCharacter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns texts per character |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_stage_directions**
> str play_stage_directions(corpusname, playname)

Get all stage directions of a play

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get all stage directions of a play
        api_response = api_instance.play_stage_directions(corpusname, playname)
        print("The response of PublicApi->play_stage_directions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_stage_directions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns plain text document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_stage_directions_with_speakers**
> str play_stage_directions_with_speakers(corpusname, playname)

Get all stage directions of a play including speakers

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get all stage directions of a play including speakers
        api_response = api_instance.play_stage_directions_with_speakers(corpusname, playname)
        print("The response of PublicApi->play_stage_directions_with_speakers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_stage_directions_with_speakers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns plain text document |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_tei**
> str play_tei(corpusname, playname)

Get TEI document of a single play

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get TEI document of a single play
        api_response = api_instance.play_tei(corpusname, playname)
        print("The response of PublicApi->play_tei:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->play_tei: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns TEI document. See [Encoding Guidelines](https://github.com/dracor-org/dracor-schema/tree/main/odd). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plays_with_character**
> List[PlayWithWikidataCharacter] plays_with_character(id)

List plays having a character identified by Wikidata ID

### Example


```python
import openapi_client
from openapi_client.models.play_with_wikidata_character import PlayWithWikidataCharacter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    id = 'Q131412' # str | 

    try:
        # List plays having a character identified by Wikidata ID
        api_response = api_instance.plays_with_character(id)
        print("The response of PublicApi->plays_with_character:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->plays_with_character: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[PlayWithWikidataCharacter]**](PlayWithWikidataCharacter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of plays. |  -  |
**400** | Invalid character ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relations_csv**
> str relations_csv(corpusname, playname)

Get relation data of a play as CSV

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get relation data of a play as CSV
        api_response = api_instance.relations_csv(corpusname, playname)
        print("The response of PublicApi->relations_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->relations_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns CSV file |  -  |
**404** | Unknown play or play does not provide relation data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relations_gexf**
> str relations_gexf(corpusname, playname)

Get relation data of a play as GEXF

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get relation data of a play as GEXF
        api_response = api_instance.relations_gexf(corpusname, playname)
        print("The response of PublicApi->relations_gexf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->relations_gexf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns GEXF file. See [Specification](https://gexf.net). |  -  |
**404** | Unknown play or play does not provide relation data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relations_graphml**
> str relations_graphml(corpusname, playname)

Get relation data of a play as GraphML

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Get relation data of a play as GraphML
        api_response = api_instance.relations_graphml(corpusname, playname)
        print("The response of PublicApi->relations_graphml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->relations_graphml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns GraphML file |  -  |
**404** | Unknown play or play does not provide relation data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_id**
> resolve_id(id)

Resolve DraCor play ID

Depending on the `Accept` header this endpoint redirects to either the RDF representation [play-rdf], the JSON meta data [play-info] or the dracor.org URL of the play identified by the `id` parameter. 

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dracor.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dracor.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApi(api_client)
    id = 'ger000023' # str | 

    try:
        # Resolve DraCor play ID
        api_instance.resolve_id(id)
    except Exception as e:
        print("Exception when calling PublicApi->resolve_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | Redirect to RDF or JSON resource or dracor.org URL. |  -  |
**404** | No play found for this ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

