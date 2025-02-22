from library import CONN, CURSOR
import datetime

class Book:
    def __init__(self, id, title, published_date, author_id, available=True):
        self.id = id
        self.title = title
        self.published_date = published_date
        self.author_id = author_id
        self.available = available

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a string and 1 or more characters long.")
        self._title = value

    @property
    def published_date(self):
        return self._published_date

    @published_date.setter
    def published_date(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("Published date must be a YYYY-MM-DD.")
        self._published_date = value

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Author ID must be an integer greater than 0.")
        self._author_id = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Available must be a boolean.")
        self._available = value

    def save(self):
        CURSOR.execute("""
              INSERT INTO books (title, published_date, author_id, available) VALUES (?, ?, ?, ?)
        """, (self.title, self.published_date, self.author_id, self.available))
        self.id = CURSOR.lastrowid
        CONN.commit()

    # ORM Methods
    @classmethod
    def create(cls, title, published_date, author_id):
        book = cls(None, title, published_date, author_id, True)
        book.save()
        return book

    @classmethod
    def delete(cls, book_id):
        CURSOR.execute("""
            DELETE FROM books WHERE id = ?
        """, (book_id,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        CURSOR.execute("""
            SELECT * FROM books
        """)
        books = CURSOR.fetchall()
        return [
            cls(
                id=row[0],
                title=row[1],
                published_date=datetime.datetime.strptime(row[2], "%Y-%m-%d").date(),
                author_id=row[3],
                available=bool(row[4])
            )
            for row in books
        ]

    @classmethod
    def find_by_id(cls, book_id):
        CURSOR.execute("""
            SELECT * FROM books WHERE id = ?
        """, (book_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(
                id=row[0],
                title=row[1],
                published_date=datetime.datetime.strptime(row[2], "%Y-%m-%d").date(),
                author_id=row[3],
                available=bool(row[4])
            )
        else:
            return None

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                published_date DATE NOT NULL,
                author_id INTEGER NOT NULL,
                available BOOLEAN NOT NULL CHECK (available IN (0, 1)),
                FOREIGN KEY (author_id) REFERENCES authors (id)
            )
        """)
        CONN.commit()
