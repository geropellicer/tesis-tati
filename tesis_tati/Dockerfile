FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update; apt-get --assume-yes install binutils libproj-dev gdal-bin graphviz python3-psycopg2 postgresql-client
RUN pip install pipenv

ENV APP_HOME=/code
# Set work directory
WORKDIR ${APP_HOME}

RUN useradd -m container_user
RUN chown -R container_user:container_user ${APP_HOME}

# Copy project
COPY . ${APP_HOME}/

# Install dependencies
RUN pipenv install --system

# Copy entrypoint
COPY ./entrypoint.sh ./entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]