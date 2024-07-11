from library.models.author import Author
from library.models.book import Book
import datetime

class Cli:
    def start(self):
        while True:
            print("Library Management System")
            print("1. Manage Authors")
            print("2. Manage Books")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_authors()
            elif choice == '2':
                self.manage_books()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    def manage_authors(self):
        while True:
            print("Author Management")
            print("1. Create Author")
            print("2. Delete Author")
            print("3. View All Authors")
            print("4. Find Author by ID")
            print("5. View Books by Author")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_author()
            elif choice == '2':
                self.delete_author()
            elif choice == '3':
                self.view_all_authors()
            elif choice == '4':
                self.find_author_by_id()
            elif choice == '5':
                self.view_books_by_author()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Try again.")

    def create_author(self):
        name = input("Enter author name: ")
        birth_date_str = input("Enter birth date (YYYY-MM-DD): ")
        try:
            birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            # parses a string into a datetime object
            author = Author.create(name, birth_date)
            print(f"Author {author.name} created successfully with ID {author.id}.")
        except ValueError:
            print("Invalid date format. Enter date in YYYY-MM-DD format.")

    def delete_author(self):
        author_id = input("Enter author ID to delete: ")
        if self.validate_id(author_id):
            #validate_id function is defined in the Cli class at the end of the class
            Author.delete(int(author_id))
            # converts a string to an integer
            print("Author deleted successfully.")
        else:
            print("Invalid ID. Enter a valid ID.")

    def view_all_authors(self):
        authors = Author.get_all()
        for author in authors:
            print(f"ID: {author.id}, Name: {author.name}, Birth Date: {author.birth_date}")

    def find_author_by_id(self):
        author_id = input("Enter author ID: ")
        if self.validate_id(author_id):
            author = Author.find_by_id(int(author_id))
            if author:
                print(f"ID: {author.id}, Name: {author.name}, Birth Date: {author.birth_date}")
            else:
                print("Author not found.")
        else:
            print("Invalid ID. Enter a valid ID.")

    def view_books_by_author(self):
        author_id = input("Enter author ID: ")
        if self.validate_id(author_id):
            books = Book.get_all()
            for book in books:
                if book.author_id == int(author_id):
                    print(f"ID: {book.id}, Title: {book.title}, Published Date: {book.published_date}, Available: {book.available}")
        else:
            print("Invalid ID. Enter a valid ID.")

    def manage_books(self):
        while True:
            print("Book Management")
            print("1. Create Book")
            print("2. Delete Book")
            print("3. View All Books")
            print("4. Find Book by ID")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_book()
            elif choice == '2':
                self.delete_book()
            elif choice == '3':
                self.view_all_books()
            elif choice == '4':
                self.find_book_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")

    def create_book(self):
        title = input("Enter book title: ")
        published_date_str = input("Enter published date (YYYY-MM-DD): ")
        author_id = input("Enter author ID: ")
        if self.validate_id(author_id):
            try:
                published_date = datetime.datetime.strptime(published_date_str, "%Y-%m-%d").date()
                book = Book.create(title, published_date, int(author_id))
                print(f"Book {book.title} created successfully with ID {book.id}.")
            except ValueError:
                print("Invalid date format. Enter date in YYYY-MM-DD format.")
        else:
            print("Invalid ID. Enter a valid ID.")

    def delete_book(self):
        book_id = input("Enter book ID to delete: ")
        if self.validate_id(book_id):
            Book.delete(int(book_id))
            print("Book deleted successfully.")
        else:
            print("Invalid ID. Enter a valid ID.")

    def view_all_books(self):
        books = Book.get_all()
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Published Date: {book.published_date}, Author ID: {book.author_id}, Available: {book.available}")

    def find_book_by_id(self):
        book_id = input("Enter book ID: ")
        if self.validate_id(book_id):
            book = Book.find_by_id(int(book_id))
            if book:
                print(f"ID: {book.id}, Title: {book.title}, Published Date: {book.published_date}, Author ID: {book.author_id}, Available: {book.available}")
            else:
                print("Book not found.")
        else:
            print("Invalid ID. Enter a valid ID.")

    def validate_id(self, id_str):
        """Helper function to validate if the input string is a valid numeric ID."""
        return id_str.isdigit()

if __name__ == '__main__':
    Cli().start()
