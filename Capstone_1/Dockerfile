# Specify base image 
FROM python:3.8.15-slim

# install pipenv
# apt-get update && apt-get install
RUN pip install pipenv

# create and set the directory
WORKDIR /app

# copy pipfile and pipfile.lock
COPY ["Pipfile", "Pipfile.lock", "./"]

# install Python dependencies
RUN pipenv install --system --deploy

# copy ML model files
COPY ["predict.py", "lr_model.bin", "./"]

# expose the port 
EXPOSE 9696

# set entrypoint instead from docker run --entrypoint=bash
# make it predict service with gunicorn
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]

