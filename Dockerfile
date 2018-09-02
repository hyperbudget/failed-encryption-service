FROM amazon/aws-eb-python:3.4.2-onbuild-3.5.1

WORKDIR /app
ADD . /app

RUN yun install gpg make glibc-devel gcc patch

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install  gunicorn

EXPOSE 8000

CMD gunicorn app:API --bind=0.0.0.0:8000
