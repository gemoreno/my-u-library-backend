from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()
User = get_user_model()

class Command(BaseCommand):
    help = 'Seed test users (4 students, 2 librarians)'

    def handle(self, *args, **kwargs):
        # Students
        for i in range(1, 5):
            email = f"s{i}@g.com"
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(
                    email=email,
                    password="lib12345",
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    role="student"
                )
                self.stdout.write(self.style.SUCCESS(f"Created student {email}"))
            else:
                self.stdout.write(f"Student {email} already exists")

        # Librarians
        for i in range(1, 3):
            email = f"l{i}@g.com"
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(
                    email=email,
                    password="lib12345",
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    role="librarian"
                )
                self.stdout.write(self.style.SUCCESS(f"Created librarian {email}"))
            else:
                self.stdout.write(f"Librarian {email} already exists")
