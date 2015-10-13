#!/bin/bash
sudo apt-get install python-dev python-setuptools libjpeg62-dev zlib1g-dev libfreetype6-dev python-virtualenv build-essential
virtualenv env
source env/bin/activate
python manage.py syncdb
python manage.py runserver

