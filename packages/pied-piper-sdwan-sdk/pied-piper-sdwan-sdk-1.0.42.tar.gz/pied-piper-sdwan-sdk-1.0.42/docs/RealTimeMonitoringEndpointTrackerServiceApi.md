# openapi_client.RealTimeMonitoringEndpointTrackerServiceApi

All URIs are relative to *https://1.1.1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoint_tracker_info**](RealTimeMonitoringEndpointTrackerServiceApi.md#get_endpoint_tracker_info) | **GET** /device/endpointTracker | 


# **get_endpoint_tracker_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_endpoint_tracker_info(device_id)



Get endpoint tracker info from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_endpoint_tracker_service_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_endpoint_tracker_service_api.RealTimeMonitoringEndpointTrackerServiceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_endpoint_tracker_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringEndpointTrackerServiceApi->get_endpoint_tracker_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

