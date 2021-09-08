from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

def getValue(context, key):
    if key in context:
        return context[key]
    else:
        raise Exception(key+' does not exist in context')

class VpcExampleStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        config = self.node.try_get_context('config')
        if not config:
            raise Exception('No config value defined')
        print("Running for "+config+"...")

        context = self.node.try_get_context(config)
        if not context:
            raise Exception('No context for config defined')

        vpc_cidr = getValue(context, "vpc_cidr")
        vpc_name = getValue(context, "vpc_name")
        num_of_azs = getValue(context, "num_of_azs")

        vpc = ec2.Vpc(self, vpc_name,
            cidr=vpc_cidr,
            max_azs=float(num_of_azs),
            nat_gateways=1,
            subnet_configuration=[ 
                { "cidrMask": 24, "name": "Public", "subnetType": ec2.SubnetType.PUBLIC, }, 
                { "cidrMask": 24, "name": "Private", "subnetType": ec2.SubnetType.PRIVATE, }, 
                { "cidrMask": 24, "name": "Services", "subnetType": ec2.SubnetType.PRIVATE, }, 
                { "cidrMask": 24, "name": "Protected", "subnetType": ec2.SubnetType.ISOLATED, } 
            ]
        )

        cdk.Tags.of(vpc).add("Name", vpc_name)
