from sqlalchemy.orm import Session
from models import Book
from sqlalchemy import desc, func, asc

from models import Base, Book, Author
from setup import get_session


def books_with_most_pages(limit=10):
    with get_session() as session:
        books = session.query(Book).order_by(desc(Book.page_amount)).limit(limit).all()
        for book in books:
            print(book)


def average_page_amount():
    with get_session() as session:
        average = session.query(func.avg(Book.page_amount)).scalar()
        print(average)


def youngest_author():
    with get_session() as session:
        youngest = session.query(Author).order_by(asc(Author.birth_date)).first()
        print(youngest)


def authors_with_no_book():
    with get_session() as session:
        authors = (session.query(Author).outerjoin(Book).filter(Book.id.is_(None)).all())
        for author in authors:
            print(author)