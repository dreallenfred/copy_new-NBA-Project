#!/bin/bash
rm -rf ./db.sqlite3
rm -rf ./nba/migrations
python manage.py makemigrations nba
python manage.py migrate
