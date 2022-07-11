import boto3
import json

def handler(event, _context):
    request_body = json.loads(event['body'])
    product_code = request_body['product_code']
    name = request_body['name']
    if product_code == None or name == None:
             return {"body":"product_code and name are required", "statusCode": 400}
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('products')
        table.put_item(
                Item = {
                    'product_code': product_code,
                    'name': name,
                }
            )
        return {"body":"Product sucessfully created", "statusCode": 200}
    except:
        return {"body": "Internal server error", "statusCode": 500}
    