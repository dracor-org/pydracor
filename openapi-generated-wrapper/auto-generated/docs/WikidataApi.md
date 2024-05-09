# openapi_client.WikidataApi

All URIs are relative to *https://dracor.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wikidata_author_info**](WikidataApi.md#wikidata_author_info) | **GET** /wikidata/author/{id} | List author information from Wikidata
[**wikidata_mixnmatch**](WikidataApi.md#wikidata_mixnmatch) | **GET** /wikidata/mixnmatch | Endpoint for Wikidata Mix&#39;n&#39;match


# **wikidata_author_info**
> object wikidata_author_info(id)

List author information from Wikidata

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
    api_instance = openapi_client.WikidataApi(api_client)
    id = 'Q34628' # str | 

    try:
        # List author information from Wikidata
        api_response = api_instance.wikidata_author_info(id)
        print("The response of WikidataApi->wikidata_author_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikidataApi->wikidata_author_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Author information |  -  |
**404** | Invalid or non existing author ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wikidata_mixnmatch**
> str wikidata_mixnmatch()

Endpoint for Wikidata Mix'n'match

See https://meta.wikimedia.org/wiki/Mix'n'match/Import.

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
    api_instance = openapi_client.WikidataApi(api_client)

    try:
        # Endpoint for Wikidata Mix'n'match
        api_response = api_instance.wikidata_mixnmatch()
        print("The response of WikidataApi->wikidata_mixnmatch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WikidataApi->wikidata_mixnmatch: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | List of plays (id, name, q [wikidata ID]). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

