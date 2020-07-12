from aws_cdk import core
from aws_cdk import (aws_s3,aws_apigateway, aws_lambda)


class S3LambdaExampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        # Create Lambda
        my_lambda = aws_lambda.Function(
            self, 'Handler',
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.asset('lambda'),
            handler='mylambda.handler'
        )

        # Create S3 Bucket
        my_s3_bucket = aws_s3.Bucket(self, 'my_s3_bucket')
        my_s3_bucket.grant_read(my_lambda) # Grant read permistion to my_lambda

        #Add Bucket Name
        my_lambda.add_environment('BUCKET_NAME',my_s3_bucket.bucket_name)

        # API Gateway
        aws_apigateway.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )
