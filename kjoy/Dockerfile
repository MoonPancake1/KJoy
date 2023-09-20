# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /usr/src/kjoy

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies, cffi
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev linux-headers g++ libffi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/kjoy/entrypoint.sh
RUN chmod +x /usr/src/kjoy/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/kjoy/entrypoint.sh"]