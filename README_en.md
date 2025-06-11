# Python Cloud Function Example

This is an example of integrating API Gateway and Cloud Functions using the operation context.
As operation context, we use the `context` parameter in the [x-yc-apigateway-integration:cloud_functions](https://yandex.cloud/docs/api-gateway/concepts/extensions/cloud-functions) extension part of the OpenAPI specification. The value of this parameter can have a nested structure, but is limited to 2 KB.
The operation context allows you to parameterize your integration function for generic OpenAPI specification operations.
In our example, the API Gateway provides the value of the `/{name}` request path parameter to the function in the `requestContext.apiGateway.operationContext.name` field of the [operation context](https://yandex.cloud/docs/functions/concepts/function-invoke#request).

## Running

1. Create a cloud function, select Python as the runtime environment, and paste the code from [handler.py](handler.py)
2. Create an API Gateway and paste the specification from [openapi-example.yaml](openapi-example.yaml), inserting the ID of the previously created function into it.

To start testing, open `https://<created API gateway domain>/world` in your browser.

## Running the function from your terminal

    python3 main.py <json request> [<json context>]

## Tests

    python3 test.py
