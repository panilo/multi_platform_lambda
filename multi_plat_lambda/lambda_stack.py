from aws_cdk import (    
    Stack,
    aws_lambda,
    aws_ecr_assets as ecr
)
from constructs import Construct

class LambdaMultiplatDemStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_function = aws_lambda.DockerImageFunction(
            self, 
            "MyDifferentPlatformFn",
            code=aws_lambda.DockerImageCode.from_image_asset(
              ".",
              platform=ecr.Platform.LINUX_ARM64
            ),
            architecture=aws_lambda.Architecture.ARM_64,
        )
