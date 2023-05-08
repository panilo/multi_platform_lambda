#!/usr/bin/env python3
import os

import aws_cdk as cdk

from multi_plat_lambda.lambda_stack import LambdaMultiplatDemStack


app = cdk.App()
LambdaMultiplatDemStack(app, "LambdaMultiplatDemStack")

app.synth()
