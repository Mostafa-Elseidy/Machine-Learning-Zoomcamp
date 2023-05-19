# Fashion Classification with Keras and TensorFlow Lite 
**Create a web Service that classify clothes images from a URL**    
- Build and train a classification model on notebook.ipynb
- Convert keras model to TFLite 
- Remove TF dependencies
- Build a Lambda handler function with Flask
- Containarize the application
- Deploy as a serveless function on AWS
- Turning Lambda function to a web service

## Create a virtual environment 
```sh
python -m venv .clothes_tflite
```  
### activate it 
```sh
source .clothes_tflite/bin/activate
```  
### Setup 
install requirements
```sh
pip install -r requirements.txt
```     
## Lambda handler
- preprocess input image
- load image from url
- predict

## Containerization
use base image from [AWS ECR Public Gallery]('https://gallery.ecr.aws/lambda/python')
```sh
docker build -t clothing-model . 
```
### test it with test.py 

## AWS Lambda Function
Create function from a container image
### upload the container to Amazon ECR "Elastic Container Registry"
Install AWS CLI
```sh
pip install awscli
aws configure
```
Configure 
```sh
aws configure
```
Create a container registry
```sh
aws ecr create-repository --repository-name fashion-tflite
```

copy the repo URI

get login
```sh
aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,\}/PASSWORD/g'
```
login to registry with docker `generated from above`

```sh
$(aws ecr get-login --no-include-email)
```
prep repo_uri
```sh
ACCOUNT=
REGION=
REGISTRY=fashion-tflite
PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}

TAG=clothing-model-exception-v1-001
REMOTE_URI=${PREFIX}:${TAG}
```

tag the container
```sh
docker tag clothing-model:latest ${REMOTE_URI}
```
push container to ecr
```sh
docker push ${REMOTE_URI}
```

## AWS Lambda Function
create from web console
- from a container image
    - function name
    - URI
    - architecture x86_64

## Exposing the Lambda Function
### AWS API Gateway
- create a REST API
- create /predict resource
- create POST method
- test it    

### Deploy API   
- new deployment stage
- test it with the generated url
```sh
python test_aws_api.py
```