#!/bin/bash

NAME="validator"                              #Name of the application (*)
DJANGODIR=/srv/validator-api                          # Django project directory (*)
SOCKFILE=/srv/anmp/run/gunicorn.sock     # we will communicate using this unix socket (*)
USER=ubuntu                                   # the user to run as (*)
GROUP=www-data                                # the group to run as (*)
NUM_WORKERS=6                                 # how many worker processes should Gunicorn spawn (*)
DJANGO_WSGI_MODULE=config.wsgi                # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
. /srv/.virtualenvs/validator/bin/activate

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
