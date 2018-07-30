FROM python:3.6
MAINTAINER jeremy.harris@zenosmosis.com

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get update \
  && apt-get install -y \
  nodejs \
  libpq-dev \
  postgresql-client \
  postgresql-client-common \
  python3-psycopg2 \
  # Clean up apt-cache
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /src/*.deb 

# Install Python project dependencies
RUN pip install Flask SQLAlchemy psycopg2-binary

WORKDIR /app

# RUN groupadd -r app && useradd -r -g app app \
#    && chown -R app:app /app

# USER app

ADD . /app

ENV FLASK_APP=backend/python/server.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]