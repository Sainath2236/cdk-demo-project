from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_apigateway as apigateway,
    aws_lambda as aws_lambda
)
from constructs import Construct
import os

class DemoPythonCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.fin_cloud_sales_api = apigateway.RestApi(
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

        self.fin_cloud_sales_api.root.add_method(
            'GET',
            write_product_integration
        )


