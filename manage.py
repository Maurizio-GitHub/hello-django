# This file has been generated, along with django_todo folder, after entering
# 'pip3 install django' and 'django-admin startproject django_todo .'
# commands in the Terminal. It is a management utility.

# We can use that 'manage.py' by entering 'python3 manage.py runserver' in the
# Terminal. It will tell us that a service is listening on port 8000 but
# it is not exposed. So, we will expose that and then click on open browser.

# Migrations are Django's way of converting Python code into database
# operations. In other words, when we need to make changes to a database
# connected to a Django project, instead of running raw SQL commands or
# using some other database language, Django will do everything for us
# and all we need to do is write Python code. The reason that we keep
# getting that warning when we run our project is because Django recognizes
# that, even though we have created a new project and started an app, we
# have not actually done anything to set up the SQLite database that it
# created for us: it is telling us that we need to run all the initial
# built-in database operations in order for our database to work properly.

# !/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# To install Heroku CLI in Gitpod:
# - curl https://cli-assets.heroku.com/install.sh | sh

# - use the login command: heroku login -i
# - enter your Heroku email
# - enter your Heroku API as password

# To view any other commands, just type: heroku

# If you need to know how any of these other commands work, just type:
# 'heroku' followed by the command and then the 'help' command. Example:
# heroku apps help

# DATABASE:
# db.sqlite3 has been acting as our database throughout this walk-through.
# This is fine for local development, but it will not work in production,
# because Heroku uses an ephemeral file system that it is wiped clean every
# time Heroku runs updates or we redeploy our app. Since db.sqlite3 is a
# file-based database, we will lose our entire database every time this
# happens because, when the file system is wiped, the file will be deleted.
# Therefore, we will use an add-on for Heroku, which will allow us to use a
# server-based database called Postgres that will be separated from our
# application, so it will survive even if the application server is destroyed.

# To use Postgres in our app, we need to install a package called psycopg2:
# pip3 install psycopg2-binary

# We also need a tool that replaces the development server once the app is
# deployed to Heroku. Gunicorn will act as our web server:
# pip3 install gunicorn

# Finally, we need a file to let Heroku know which packages to install:
# pip3 freeze --local > requirements.txt

# To create a new app on Heroku:
# heroku apps:create APPNAME --region eu

# To view all your apps:
# heroku apps

# To shows you the key remote urls:
# git remote -v

# There are two key remote urls here:
# one for pushing code to Heroku; one for fetching code from Heroku.

# This tells us that when we use the command 'git push heroku master',
# it will be pushed to the master branch at the relevant url.
# If we use the command 'git push origin master',
# it would go to the other remote url.

# To connect our database to our workspace, add this to env.py:
# import os
# os.environ.setdefault("DATABASE_URL", "my_copied_database_url")

# FOLLOWING STEPS

# Install the dj-database-url package for Django to parse the URL got above:
# pip3 install dj_database_url

# Add it to our requirements.txt:
# pip3 freeze --local > requirements.txt

# Import the package and the env.py file at the top of 'settings.py':
# from pathlib import Path
# import os
# import dj_database_url
# import env

# Comment out the default database setting and replace it to use the
# DATABASE_URL environment variable in 'settings.py'; in this case:
# DATABASES =
# {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

# Run the migrate command to build the database according to the model created:
# python3 manage.py migrate

# In case we do not have static files for Heroku to collect:
# heroku config:set DISABLE_COLLECTSTATIC=1

# After that, we can push to Heroku:
# git push heroku main

# In case of issues, we use this command to check the deployment logs:
# heroku logs --tail

# In case the issue is that we have not told Heroku that we want this to be a
# web-app with a web server, just remember that we installed 'gunicorn' to act
# as our web server. However, we have not told 'gunicorn' to start yet.
# To do that, we can create a special file called a 'Procfile'.

# Into Procfile, we write the following code to tell 'gunicorn' to run,
# using our project's wsgi module, which allows it to handle HTTP requests
# like run-server does in our local development environment:
# web: gunicorn django_todo.wsgi:application

# We also need to to add the host name of our Heroku app to the allowed host
# list in 'settings.py'. This list allows Django to ensure that HTTP requests
# are coming from domain names it trusts:
# 'django-to-do-walk-through.herokuapp.com'

# After that, we need to commit once again!
