mkdir basic-example
cd basic-example
cdk init --language python
source .venv/bin/activate ## Python only
pip3 install -r requirements.txt ## Python only
pip3 install aws-cdk.aws-ssm ## python only
cdk synth
cdk deploy