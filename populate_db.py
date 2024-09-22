import random

from faker import Faker
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Book, Author
from setup import get_session


class PopulateDatabase:
    def __init__(self):
        self.fake = Faker()
        self.book_release_date_start = date(year=1980, month=1, day=1)
        self.author_birth_date_start = date(year=1880, month=1, day=1)
        self.author_birth_date_end = date(year=1966, month=1, day=1)
        self.categories = ['fantasy', 'thriller', 'fiction', 'mystery', 'science fiction', 'horror', 'adventure',
                           'history', 'comedy', 'romance', 'biography']

    def populate_books(self, num_books=1000):
        books = []
        for i in range(1, num_books+1):
            name = f'bookName_{i}'
            category = random.choice(self.categories)
            page_amount = random.randint(75, 800)
            release_date = self.fake.date_between(start_date=self.book_release_date_start, end_date='now')
            author_id = random.randint(1, 500)

            book = Book(name=name, category=category, page_amount=page_amount, release_date=release_date,
                        author_id=author_id)
            books.append(book)

        self._commit_to_db(books)

    def populate_authors(self, num_authors=500):
        authors = []
        for _ in range(1, num_authors+1):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()
            birth_date = self.fake.date_between(start_date=self.author_birth_date_start,
                                                end_date=self.author_birth_date_end)
            birth_place = self.fake.country()

            author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date, birth_place=birth_place)
            authors.append(author)

        self._commit_to_db(authors)

    def _commit_to_db(self, records):
        with get_session() as session:
            session.add_all(records)
            session.commit()

    def ensure_db_populated(self):
        with get_session() as session:
            book_count = session.query(Book).count()
            author_count = session.query(Author).count()

            if not (book_count == 1000 and author_count == 500):
                session.query(Book).delete()
                session.query(Author).delete()
                session.commit()
                self.populate_books()
                self.populate_authors()
