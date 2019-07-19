FROM python:3.7-alpine3.10

MAINTAINER Omambia Dauglous
#python unbuffured environement allows python to run outputs directly
ENV PYTHONUNBUFFERED 1

#install our dependancies
COPY ./requirements.txt /requirements.txt 
RUN apk add --update --no-cache postgresql-client 
RUN apk add --update --no-cache --virtual .temp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r ./requirements.txt
#remove temprary requirements
RUN apk del .temp-build-deps
# making working directories

RUN mkdir /app  
WORKDIR /app 
COPY ./app /app

# create use 
# to only run our application only -D 
RUN adduser -D user 
USER user 



