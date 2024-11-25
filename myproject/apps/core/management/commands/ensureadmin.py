from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Ensures the provided admin user exists, creating it with the provided password if it doesn't"

    def add_arguments(self, parser):
        parser.add_argument("--username", help="Username")
        parser.add_argument("--email", help="Email", default=None)
        parser.add_argument("--password", help="Password")

    def handle(self, *args, **options):
        user = get_user_model()
        if not user.objects.filter(username=options["username"]).exists():
            print(self.style.NOTICE("Superuser does not exist; creating it"))
            user.objects.create_superuser(
                username=options["username"],
                email=options["email"],
                password=options["password"],
            )
