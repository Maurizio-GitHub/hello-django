# This file has been generated, along with django_todo folder, after entering
# 'pip3 install django' and 'django-admin startproject django_todo .'
# commands in the Terminal. It is a management utility.

# We can use that 'manage.py' by entering 'python3 manage.py runserver' in the
# Terminal. It will tell us that a service is listening on port 8000 but
# it is not exposed. So, we will expose that and then click on open browser.


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
