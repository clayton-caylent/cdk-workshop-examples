mkdir vpc-example
cd vpc-example
cdk init --language python
source .venv/bin/activate ## Python only
pip3 install -r requirements.txt ## Python only
pip3 install aws-cdk.aws-ec2 ## python only
cdk synth -c config=dev
cdk deploy -c config=dev