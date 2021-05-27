FROM python:3.8

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

ENV FLASK_APP=./src
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1

RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install


CMD ["pipenv", "run", "flask", "run"]