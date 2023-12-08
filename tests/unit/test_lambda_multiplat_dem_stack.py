import aws_cdk as core
import aws_cdk.assertions as assertions

from multi_plat_lambda.lambda_stack import LambdaMultiplatDemStack

def test_stack_synth():
    app = core.App()
    stack = LambdaMultiplatDemStack(app, "lambda-multiplat-dem")
    template = assertions.Template.from_stack(stack)

