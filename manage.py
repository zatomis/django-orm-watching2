import os
from environs import Env
from django.core.management import execute_from_command_line
import sys

if __name__ == "__main__":
    env = Env()
    env.read_env(".env", recurse=False)
    key = env.str("SECRET_KEY")
    DEBUG = env.bool("DEBUG", default=False)
    SECRET_KEY = env.str("SECRET_KEY")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # execute_from_command_line('manage.py runserver 127.0.0.1:8000'.split())
