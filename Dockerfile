FROM python:3.7-alpine3.10

MAINTAINER Omambia Dauglous
#python unbuffured environement allows python to run outputs directly
ENV PYTHONUNBUFFERED 1

#install our dependancies
COPY ./requirements.txt /requirements.txt 
RUN pip install -r ./requirements.txt
# making working directories
RUN mkdir /app  
WORKDIR /app 
COPY ./app /app

# create use 
# to only run our application only -D 
RUN adduser -D user 
USER user 



