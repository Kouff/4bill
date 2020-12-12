FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /4bill

COPY . /4bill
RUN pip install -r /4bill/requirements.txt
