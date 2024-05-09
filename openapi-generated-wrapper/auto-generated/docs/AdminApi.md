# openapi_client.AdminApi

All URIs are relative to *https://dracor.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_corpus**](AdminApi.md#delete_corpus) | **DELETE** /corpora/{corpusname} | Remove corpus from database
[**load_corpus**](AdminApi.md#load_corpus) | **POST** /corpora/{corpusname} | Load corpus data from its repository
[**play_delete**](AdminApi.md#play_delete) | **DELETE** /corpora/{corpusname}/plays/{playname} | Remove a single play from the corpus
[**play_tei_put**](AdminApi.md#play_tei_put) | **PUT** /corpora/{corpusname}/plays/{playname}/tei | Add new or update existing TEI document
[**post_corpora**](AdminApi.md#post_corpora) | **POST** /corpora | Add new corpus


# **delete_corpus**
> delete_corpus(corpusname)

Remove corpus from database

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
    api_instance = openapi_client.AdminApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 

    try:
        # Remove corpus from database
        api_instance.delete_corpus(corpusname)
    except Exception as e:
        print("Exception when calling AdminApi->delete_corpus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 

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
**200** | Corpus deleted |  -  |
**404** | Corpus not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_corpus**
> object load_corpus(corpusname, load_corpus_request=load_corpus_request)

Load corpus data from its repository

This endpoint requires authorization. Posting `{\"load\": true}` to the corpus URI reloads the data for this corpus from its repository (if defined).

### Example


```python
import openapi_client
from openapi_client.models.load_corpus_request import LoadCorpusRequest
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
    api_instance = openapi_client.AdminApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    load_corpus_request = {"load": true}
 # LoadCorpusRequest |  (optional)

    try:
        # Load corpus data from its repository
        api_response = api_instance.load_corpus(corpusname, load_corpus_request=load_corpus_request)
        print("The response of AdminApi->load_corpus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->load_corpus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **load_corpus_request** | [**LoadCorpusRequest**](LoadCorpusRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Corpus update has been scheduled |  -  |
**404** | Corpus not found |  -  |
**409** | Corpus update could not be scheduled. This is the response when another update has not yet finished. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_delete**
> play_delete(corpusname, playname)

Remove a single play from the corpus

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
    api_instance = openapi_client.AdminApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'lessing-emilia-galotti' # str | Name parameter (or \"slug\") of the play as provided in the `name` property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint. 

    try:
        # Remove a single play from the corpus
        api_instance.play_delete(corpusname, playname)
    except Exception as e:
        print("Exception when calling AdminApi->play_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**| Name parameter (or \&quot;slug\&quot;) of the play as provided in the &#x60;name&#x60; property of the result objects of the [/corpora/{corpusname}](#/public/list-corpus-content) endpoint.  | 

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
**200** | Play has been removed |  -  |
**404** | No such play under this URI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_tei_put**
> str play_tei_put(corpusname, playname, body=body)

Add new or update existing TEI document

When sending a PUT request to a new play URI, the request body is stored in the database as a new document accessible under that URI. If the URI already exists the corresponding TEI document is updated with the request body.  The `playname` parameter of a new URI must consist of lower case ASCII characters, digits and/or dashes only. 

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
    api_instance = openapi_client.AdminApi(api_client)
    corpusname = 'ger' # str | Short name of the corpus as provided in the `name` property of the result objects from the [/corpora](#/public/list-corpora) endpoint 
    playname = 'playname_example' # str | 
    body = 'body_example' # str | TEI document (optional)

    try:
        # Add new or update existing TEI document
        api_response = api_instance.play_tei_put(corpusname, playname, body=body)
        print("The response of AdminApi->play_tei_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->play_tei_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corpusname** | **str**| Short name of the corpus as provided in the &#x60;name&#x60; property of the result objects from the [/corpora](#/public/list-corpora) endpoint  | 
 **playname** | **str**|  | 
 **body** | **str**| TEI document | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TEI document has been stored |  -  |
**400** | The request body is not a valid TEI document or the &#x60;playname&#x60; is invalid. |  -  |
**404** | There is no corpus with the given &#x60;corpusname&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_corpora**
> object post_corpora(post_corpora_request=post_corpora_request)

Add new corpus

### Example


```python
import openapi_client
from openapi_client.models.post_corpora_request import PostCorporaRequest
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
    api_instance = openapi_client.AdminApi(api_client)
    post_corpora_request = {
  "name": "rus",
  "title": "Russian Drama Corpus",
  "repository": "https://github.com/dracor-org/rusdracor"
}
 # PostCorporaRequest | The meta data for the new corpus can be provided in either JSON or XML format. The JSON structure is a straightforward object providing corpus name, title and (optionally) a repository URL. The XML format needs to be a TEI document with `teiCorpus` as its root element. The corpus title needs to be provided in the `titleStmt` while the name and repo URL are encoded in particular `idno` elements in the `publicationStmt` (see example).  NB: Contrary to the TEI schema our teiCorpus document must not contain the `TEI` elements for individual plays.  (optional)

    try:
        # Add new corpus
        api_response = api_instance.post_corpora(post_corpora_request=post_corpora_request)
        print("The response of AdminApi->post_corpora:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->post_corpora: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_corpora_request** | [**PostCorporaRequest**](PostCorporaRequest.md)| The meta data for the new corpus can be provided in either JSON or XML format. The JSON structure is a straightforward object providing corpus name, title and (optionally) a repository URL. The XML format needs to be a TEI document with &#x60;teiCorpus&#x60; as its root element. The corpus title needs to be provided in the &#x60;titleStmt&#x60; while the name and repo URL are encoded in particular &#x60;idno&#x60; elements in the &#x60;publicationStmt&#x60; (see example).  NB: Contrary to the TEI schema our teiCorpus document must not contain the &#x60;TEI&#x60; elements for individual plays.  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns corpus metadata |  -  |
**409** | Corpus already exists |  -  |
**400** | Posted data lacks required properties or is malformed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

