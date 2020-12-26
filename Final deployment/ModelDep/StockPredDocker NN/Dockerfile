#I specify the parent base image which is the python version 3.7
FROM python:3.7

MAINTAINER Aman Kumar <amank56@gmail.com>

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /

# copy requirements.txt
COPY ./requirements.txt /requirements.txt
COPY ./app.py /app.py
COPY ./model.pkl /model.pkl


WORKDIR /templates
COPY ./templates/index.html /templates/index.html

WORKDIR /
# install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# set work directory
WORKDIR /

# set app port
EXPOSE 8080

ENTRYPOINT [ "python" ] 

# Run app.py when the container launches
CMD [ "app.py","run","--host","0.0.0.0"] 