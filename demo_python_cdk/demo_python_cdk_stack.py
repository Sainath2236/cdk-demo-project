from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_apigateway as apigateway,
    aws_lambda as aws_lambda,
    aws_dynamodb as dynamodb
)
from constructs import Construct
import os

class DemoPythonCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.products_api = apigateway.RestApi(
            self,
            "product-api",
            deploy=True,
            endpoint_types=[apigateway.EndpointType.REGIONAL]
        )


        self.lambda_fn =aws_lambda.Function(
            self,
            "WriteProductsLamndaHandler",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            handler="index.handler",
            code=aws_lambda.Code.from_asset("demo_python_cdk/runtime"),
            function_name="write-products-lambda-function"
  
        )
        write_product_integration = apigateway.LambdaIntegration(self.lambda_fn)

        products = self.products_api.root.add_resource("products")
        products.add_method("POST", write_product_integration)

        products_table = dynamodb.Table(self, "ProductTabel",
        partition_key=dynamodb.Attribute(name="product_code", type=dynamodb.AttributeType.STRING),
        table_name="products"
        )
        products_table.grant_read_write_data(self.lambda_fn)

