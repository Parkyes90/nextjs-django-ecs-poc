# Image
FROM python:3.10-slim as builder

## python deps
RUN pip install --no-cache-dir --upgrade pip==22.0.03 && \
    pip install --no-cache-dir pipenv==2022.1.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY Pipfile* ./

RUN pipenv install --system --ignore-pipfile

EXPOSE 8000

COPY . .

FROM builder as development
RUN pipenv install --system --dev --ignore-pipfile
CMD gunicorn config.asgi.dev:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --log-level debug --access-logfile - --error-logfile - --reload

FROM builder as production
CMD gunicorn config.asgi.prod:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --log-level info --access-logfile - --error-logfile -
