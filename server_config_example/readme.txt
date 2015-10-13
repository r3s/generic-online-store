Installation:
sudo apt-get python-virtualenv build-essential python-setuptools
sudo apt-get build-dep python-imaging nginx supervisor
pip install -r requirements.txt

Database setup:
use default sqlite3 database or configure the database settings in settings.py

Test setup:
python manage.py migrate
python manage.py runserver


Production setup:
Modify config/nginx_vhost and place it to nginx sites-enabled directory
modify config/uwsgi.ini
modify config/supervisor.conf and place it in supervisor conf.d directory
chmod the source directory and give appropriate permissions to www-data user

