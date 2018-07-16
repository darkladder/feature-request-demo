FROM python:3.6
MAINTAINER jeremy.harris@zenosmosis.com

RUN apt-get update \
    && apt-get install -y libpq-dev postgresql-client postgresql-client-common python3-psycopg2

RUN pip install Flask SQLAlchemy psycopg2-binary

WORKDIR /app

# RUN groupadd -r app && useradd -r -g app app \
#    && chown -R app:app /app

# USER app

ADD . /app

ENV FLASK_APP=backend/server.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]