# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/SamuTheCoder/XpressWay/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_payments_post**](DefaultApi.md#v1_payments_post) | **POST** /v1/payments | Create a new payment

# **v1_payments_post**
> InlineResponse201 v1_payments_post(body)

Create a new payment

Initializes a payment and returns a payment ID with pending status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1PaymentsBody() # V1PaymentsBody | 

try:
    # Create a new payment
    api_response = api_instance.v1_payments_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PaymentsBody**](V1PaymentsBody.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

