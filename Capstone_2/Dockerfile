FROM public.ecr.aws/lambda/python:3.8

COPY requirements_lambda.txt .
RUN pip install -r requirements_lambda.txt


COPY saved_models/clothing-model.tflite saved_models/clothing-model.tflite
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]