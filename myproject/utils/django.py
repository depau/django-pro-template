import os
import sys


def run_django_management(settings_module: str):
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    print(f"Using settings module: {settings_module}")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
