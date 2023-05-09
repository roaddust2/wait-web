FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apk add --no-cache \
    curl \
    gettext \
    git \
    make

WORKDIR /usr/src/wait-web

COPY requirements.txt ./

RUN pip install -r requirements.txt