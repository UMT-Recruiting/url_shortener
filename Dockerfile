FROM python:3.9.6

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

# RUN flask database init

# RUN flask databse migrate

# RUN flask database downgrade

RUN flask-init-db