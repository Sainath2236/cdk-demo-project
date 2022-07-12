import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest

from demo_python_cdk.demo_python_cdk_stack import DemoPythonCdkStack

@pytest.fixture(scope="module", name="stack_template")
def create_stack_template():
    app = core.App()
    stack = DemoPythonCdkStack(app, "demo-python-cdk")
    return assertions.Template.from_stack(stack)

def test_products_rest_api__created(stack_template):
    stack_template.has_resource_properties("AWS::ApiGateway::RestApi", {
         "EndpointConfiguration": {
                "Types": [
                    "REGIONAL"
                ]
        },
        "Name": "product-api"
    })

def test_products_lambda_created(stack_template):
        stack_template.has_resource_properties("AWS::Lambda::Function", {
            "FunctionName": "write-products-lambda-function",
            "Handler": "index.handler",
            "Runtime": "python3.7"
})

def test_products_dynamo__table_created(stack_template):
        stack_template.has_resource_properties("AWS::DynamoDB::Table", {
                "AttributeDefinitions": [{
                            "AttributeName": "product_code",
                            "AttributeType": "S"
                            }],
                "TableName": "products"
})
