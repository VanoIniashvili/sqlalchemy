from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    category: Mapped[str]
    page_amount: Mapped[int]
    release_date: Mapped[str]

    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))
    author: Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return (f"Book(id={self.id}, name={self.name}, category={self.category}, "
                f"page_amount={self.page_amount}, release_date={self.release_date})")


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    birth_date: Mapped[str]
    birth_place: Mapped[str]

    books: Mapped[List["Book"]] = relationship(back_populates="author")

    def __repr__(self):
        return (f"Author(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, "
                f"birth_date={self.birth_date}, birth_place={self.birth_place})")