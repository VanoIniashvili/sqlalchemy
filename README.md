# book and author database

this project provides a simple SQLite database for managing books and their authors. tt uses SQLAlchemy for ORM to facilitate interactions with the database

## features

- create and manage authors and books
- populate the database with sample data
- retrieve information such as:
  - books with most pages
  - average page amount of books
  - youngest author
  - authors with no books

## getting started

### installation

1. clone the repository:
   ```bash
   git clone https://github.com/VanoIniashvili/sqlalchemy.git
   cd sqlalchemy
    ```
2. install the required packages:   
   ```bash
    pip install -r requirements.txt
    ```
3. run the script:
    ```bash
    python3 main.py
    ```
