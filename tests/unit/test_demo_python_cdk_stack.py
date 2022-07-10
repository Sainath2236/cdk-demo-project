import aws_cdk as core
import aws_cdk.assertions as assertions

from demo_python_cdk.demo_python_cdk_stack import DemoPythonCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in demo_python_cdk/demo_python_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DemoPythonCdkStack(app, "demo-python-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
