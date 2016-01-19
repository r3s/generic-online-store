#  Do this first -- >  pip install fabric
#  keep the filename as "fabfile.py"
#  fab dev deploy -> runs dev method first then deploy
from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
import os

# globals
env.use_ssh_config = True
env.local_shell = "/bin/bash"
env.remote_project_root = "/dummy/path/project"
env.remote_activate_script = "source /dummy/path/env/bin/activate"

print(yellow("""

                       ^
                      / \\
                     /___\\
                    |=   =|
                    |     |
                    |  I  |
                    |     |
                    |  S  |
                    |     |
                    |  R  |
                    |     |
                    |  O  |
                    |     |
                   /|==!==|\\
                  / |==!==| \\
                 /  |==!==|  \\
                |  / ^ | ^ \  |
                | /  ( | )  \ |
                |/   ( | )   \|
                    ((   ))
                   ((  :  ))
                   ((  :  ))
                    ((   ))
                     (( ))
                      ( )
                       .
                       .

Launching ...
""", bold=True))

@task()
def dev():
    # Deploy to raspberrypi ,  "pi" is from my ssh config
    env.hosts = ['pi']
    env.remote_project_root = "/home/pi/django/generic_shop"
    env.remote_activate_script = "source /home/pi/django/generic_shop/env/bin/activate"


@task()
def updatedeps():
    with prefix(env.remote_activate_script):
        with cd(env.remote_project_root):
            run("pip install -r requirements.txt --download-cache=.pip_cache")
            print(orange("""Packages updated.""", bold=True))

@task()
def publish():
    command = "git push && git push github master && git push pi master"
    local('bash -l -c "%s"' % command)
    with cd(env.remote_project_root):
        run("umask 002 && git pull")
        print(green("""Code published :)""", bold=True))

@task()
def migrate():
    with cd(env.remote_project_root):
        with prefix(env.remote_activate_script):
            run("python manage.py migrate")
            print(green("""Database migrated :)""", bold=True))

@task()
def collectstatic():
    with cd(env.remote_project_root):
        with prefix(env.remote_activate_script):
            run("umask 002 && python manage.py collectstatic --noinput --verbosity=0")
            print(green("""Static files  updated.. ;)""", bold=True))
