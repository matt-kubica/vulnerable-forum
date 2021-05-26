FROM python:3.8

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install