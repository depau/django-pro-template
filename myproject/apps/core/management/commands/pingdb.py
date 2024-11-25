from django.core.management import BaseCommand, CommandError
from django.db import OperationalError, connection


class Command(BaseCommand):
    help = "Pings the database"

    def handle(self, *args, **options):
        try:
            connection.ensure_connection()
        except OperationalError as e:
            raise CommandError("Database unavailable") from e

        self.stdout.write(self.style.SUCCESS("Database available"))
