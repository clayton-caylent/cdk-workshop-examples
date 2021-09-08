mkdir rds-shared-construct
cd rds-shared-construct
cdk init --language python
source .venv/bin/activate ## Python only
pip3 install -r requirements.txt ## Python only
pip3 install aws-cdk.aws-rds ## python only
cdk synth -c config=dev
cdk deploy -c config=dev