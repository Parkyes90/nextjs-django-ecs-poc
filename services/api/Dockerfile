# Image
FROM python:3.10-slim

## python deps
RUN pip install --no-cache-dir --upgrade pip==22.0.03 && \
    pip install --no-cache-dir pipenv==2022.1.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY Pipfile* ./

RUN pipenv sync

COPY . .
