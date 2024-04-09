# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

RUN apt-get update && apt-get -y upgrade && apt-get clean

# Install any needed packages specified in requirements.txt
#COPY ./lib lib -- no libraries used as yet
ADD ./requirements.txt requirements.txt
RUN  pip install -r requirements.txt

COPY ./app app

RUN addgroup app \
  && adduser --disabled-password --gecos "" --home "/app" --no-create-home --ingroup app app  \
  && chown -R app:app /app

USER app

HEALTHCHECK CMD curl -f http://localhost/ || exit 1
