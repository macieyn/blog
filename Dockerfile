FROM python:3.8-slim-buster

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . app/

RUN pip install -r app/requirements.txt

