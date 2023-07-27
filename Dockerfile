FROM python:3.10.6

ENV PYTHONDONWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /code/
