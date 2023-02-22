# =============
# Builder Image
# =============

FROM python:3.10-alpine

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project
ADD . /home/app/web

WORKDIR /home/app/web/comics_finder_api

# PSQL deps
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
RUN pip install poetry
RUN poetry add gunicorn psycopg2 && poetry install
