from aws_cdk import core as cdk

from aws_cdk import core
from aws_cdk import aws_rds as rds
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_secretsmanager as sm

class RDSInstance(core.Construct):

    def __init__(self, scope: core.Construct, id: str, *, env, vpc_name, rds_name):
        super().__init__(scope, id)

        vpc = ec2.Vpc.from_lookup(self, vpc_name+"lookup",
            tags={
                "Name": vpc_name
            }
        )

        if env == 'prod':
            inst_type=ec2.InstanceType('m5.large')
            db_name='prod'
        else:
            inst_type=ec2.InstanceType('t3.large')
            db_name='dev'


        rds.DatabaseInstance(self, rds_name, 
            engine=rds.DatabaseInstanceEngine.MYSQL, 
            database_name=db_name, 
            instance_type=inst_type, 
            vpc=vpc, 
            credentials=rds.Credentials.from_generated_secret("dbadmin"),
            vpc_subnets=ec2.SubnetSelection(subnet_group_name="Private")
        )
