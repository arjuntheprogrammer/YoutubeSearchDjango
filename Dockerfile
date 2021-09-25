ARG PYTHON_VERSION=3.9-slim-buster

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./docker_conf/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker


COPY ./docker_conf/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat


COPY . /code/
