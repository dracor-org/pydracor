# openapi_client.WebhookApi

All URIs are relative to *https://dracor.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**github_webhook**](WebhookApi.md#github_webhook) | **POST** /webhook/github | GitHub Webhook


# **github_webhook**
> object github_webhook(user_agent, x_git_hub_delivery, x_git_hub_event, x_hub_signature, body=body)

GitHub Webhook

Endpoint accepting POST requests from Github (see https://developer.github.com/webhooks/). We currently only handle push events on the main branch.

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
    api_instance = openapi_client.WebhookApi(api_client)
    user_agent = 'user_agent_example' # str | 
    x_git_hub_delivery = '4e16d4dc-1d87-11e9-830d-68e2a0832130' # str | 
    x_git_hub_event = 'x_git_hub_event_example' # str | 
    x_hub_signature = 'sha1=6da21762fada5c1d0205c6e42xxxxxxxxxx357c0' # str | 
    body = None # object | Webhook payload (see https://developer.github.com/webhooks/#payloads) (optional)

    try:
        # GitHub Webhook
        api_response = api_instance.github_webhook(user_agent, x_git_hub_delivery, x_git_hub_event, x_hub_signature, body=body)
        print("The response of WebhookApi->github_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->github_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_agent** | **str**|  | 
 **x_git_hub_delivery** | **str**|  | 
 **x_git_hub_event** | **str**|  | 
 **x_hub_signature** | **str**|  | 
 **body** | **object**| Webhook payload (see https://developer.github.com/webhooks/#payloads) | [optional] 

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
**200** | Webhook delivery has been received, a status message is being returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

