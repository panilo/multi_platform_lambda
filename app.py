#!/usr/bin/env python3
import os

import aws_cdk as cdk

from multi_plat_lambda.lambda_stack import LambdaMultiplatDemStack

env_name = os.getenv("ENV_NAME")

if not env_name:
    raise ValueError("No ENV_NAME")

app = cdk.App()
LambdaMultiplatDemStack(app, f"LambdaMultiplatDemStack-{env_name}")

app.synth()
