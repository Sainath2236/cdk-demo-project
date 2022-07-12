from behave import given, when, then
import boto3
import requests
import json

AWS_DEFAULT_REGION = "ap-south-1"
PRODUCTS_LAMBDA = 'write-products-lambda-function'
# Use your deployed api url here or custom domain path(if you configure that)
API_URL = 'host_name/deployment_stage/prodcuts'

@given('there is products lambda exists')
def step_impl(context):
    # Give the aws profile name which configured in your cli
    session = boto3.Session(profile_name='my-aws')
    client = session.client('lambda', region_name=AWS_DEFAULT_REGION)
    lambda_response = client.get_function(FunctionName=PRODUCTS_LAMBDA)
    assert lambda_response['Configuration']['FunctionName'] == PRODUCTS_LAMBDA

@given('there is products dynamo table exists')
def step_impl(context):
    session = boto3.Session(profile_name='my-aws')
    client = session.client('dynamodb')
    response = client.list_tables()
    table = 'products'
    assert table in response['TableNames']

@when('I call products post api')
def step_impl(context):
    context.result  = requests.post(API_URL, json={'product_code': "p100", 'name': 'product1'})

@then('I should see the sucess response')
def step_impl(context):
     assert context.result.text == 'Product sucessfully created'

    