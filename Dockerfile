# =============
# Builder Image
# =============

FROM python:3.10-alpine as builder

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# PSQL deps
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev poetry

# Install dependencies
COPY ./pyproject.toml .
RUN poetry add gunicorn psycopg2 --lock
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Copy project
COPY . .

#########
# FINAL #
#########

# pull official base image
FROM python:3.10-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME/comics_finder_api

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app
