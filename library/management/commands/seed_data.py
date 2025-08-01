import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

from library.models import Book

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
                
        # Seed Books
        book_count = Book.objects.count()
        books_to_create = 30 - book_count if book_count < 30 else 0
        for _ in range(books_to_create):
            book = Book.objects.create(
                title=fake.sentence(nb_words=4),
                author=fake.name(),
                year_published=random.randint(1950, 2023),
                genre=random.choice(['Fiction', 'History', 'Science', 'Fantasy', 'Romance', 'Biography']),
                stock=random.randint(2, 10)
            )
            self.stdout.write(self.style.SUCCESS(f"Created book: {book.title}"))

        if books_to_create == 0:
            self.stdout.write(self.style.WARNING("Book seeding skipped: already 30 or more books in database."))
