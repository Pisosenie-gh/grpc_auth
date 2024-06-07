#!/bin/sh


./wait-for-it.sh db 5432 -- echo "Database is up"

alembic upgrade head

python server.py