#!/bin/bash

set -e
  
# wait for postgres
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done  
>&2 echo "Postgres is up - executing command"

# execute a command
if [ $1 = "manage" ]
then
    shift
    exec python manage.py $@
elif [ $1 = "install" ]
then
    shift
    exec pipenv install $@
elif [ $1 = "rungunicorn" ]
then
    shift
    cpus="$(nproc --all)"
    workers="$((($cpus * 2) + 1))"
    if [ $workers -gt 12 ]
    then
        workers="12"
    fi
    exec gunicorn tesistati.wsgi:application --bind 0.0.0.0:8002 --workers $workers
elif [ $1 = "runtests" ]
then
    exec python manage.py test
else
    exec $@
fi