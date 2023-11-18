# pull official base image
FROM python:3.9.18-alpine3.18

# set work directory
WORKDIR /usr/src/Granja

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/Granja/

# copy project
COPY . .

# run entrypoint.sh
# RUN ["chmod", "+x", "/usr/src/Granja/entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]