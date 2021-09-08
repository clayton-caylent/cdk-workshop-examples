from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from rds_shared_construct.rds import RDSInstance

class SharedConstructExampleStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        RDSInstance(self, "dev",
            env="dev",
            vpc_name="dev-vpc",
            rds_name="dev-rds"
        )

        RDSInstance(self, "dev2",
            env="dev",
            vpc_name="dev-vpc",
            rds_name="dev2-rds"
        )

