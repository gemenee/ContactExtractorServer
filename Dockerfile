# syntax=docker/dockerfile:1
FROM python:3.10

WORKDIR /server/

# install app dependencies
RUN pip install flask==2.1.* && pip install natasha

# install app
COPY . .

# final configuration
ENV FLASK_APP=run
#EXPOSE 5000
CMD flask run --host 0.0.0.0 --port 8000
