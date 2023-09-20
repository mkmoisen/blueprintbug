FROM python:3.11.5-bookworm

RUN apt update
RUN apt install vim -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
