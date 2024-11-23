FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/backend/

COPY ./ /app/backend/

RUN pip install --upgrade pip && pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

RUN apt-get update && apt-get install -y nano bash

EXPOSE 5005
