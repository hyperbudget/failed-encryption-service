FROM python:3.6.6-alpine3.8

WORKDIR /app
ADD . /app

RUN apk add --update alpine-sdk

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --user gunicorn

EXPOSE 8000

CMD "gunicorn app:API"
