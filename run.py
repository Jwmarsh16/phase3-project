from library.models.author import Author
from library.models.book import Book
from library.cli import Cli

# Create tables
Author.create_table()
Book.create_table()

# Start the CLI
Cli().start()
