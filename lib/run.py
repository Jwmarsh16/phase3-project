from models.author import Author
from models.book import Book

from cli import Cli

Author.create_table()
Book.create_table()

Cli().start()