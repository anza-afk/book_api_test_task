FROM python:3.11.4-slim

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY requirements.txt .
COPY ./entrypoint.sh /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN pip install --upgrade pip

COPY ./library/ .

RUN chmod +x /entrypoint.sh