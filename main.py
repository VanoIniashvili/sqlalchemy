from queries import books_with_most_pages, average_page_amount, youngest_author, authors_with_no_book
from populate_db import PopulateDatabase


def create_app():
    populate_database = PopulateDatabase()

    populate_database.ensure_db_populated()

    print('books with most pages:')
    books_with_most_pages()
    print('------------------------------------\naverage page amount:')
    average_page_amount()
    print('------------------------------------\nyoungest author:')
    youngest_author()
    print('------------------------------------\nauthors with no book:')
    authors_with_no_book()


if __name__ == '__main__':
    create_app()