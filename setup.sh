#!/bin/bash
# Tested on ubuntu 14.04
# Install OS libraries
sudo apt-get install python-dev python-setuptools libjpeg62-dev zlib1g-dev libfreetype6-dev python-virtualenv build-essential
# Create python virtual enviorment
virtualenv env
# Activate virtual enviorment
source env/bin/activate
# Install python libraries in virtual environment
pip install -r requirements.txt
# Create database and admin user
python manage.py syncdb
# Run development server
python manage.py runserver
