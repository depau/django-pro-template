from myproject.utils.django import run_django_management

from . import settings

if __name__ == "__main__":
    run_django_management(settings.__name__)
