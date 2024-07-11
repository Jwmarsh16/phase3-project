from models.__init__ import CONN, CURSOR

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
            raise ValueError("Title must be a non-empty string.")
        self._title = value


    @property
    def published_date(self):
        return self._published_date
    
    
    @published_date.setter
    def published_date(self, value):
        self._published_date = value


    @property
    def author_id(self):
        return self._author_id
    
    
    @author_id.setter
    def author_id(self, value):
        if hasattr(self, '_author_id') or not isinstance(value, int) or value == 0:
            raise ValueError("Author ID must be a positive integer.")
        self._author_id = value


    @property
    def available(self):
        return self._available
    
    
    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Available status must be a boolean value.")
        self._available = value


    @classmethod
    def create(cls, title, published_date, author_id):
        CURSOR.execute("INSERT INTO books (title, published_date, author_id, available) VALUES (?,?, ?,?)", 
        (title, published_date, author_id, True))
        CONN.commit()
        

    @classmethod
    def delete(cls, book_id):
        CURSOR.execute("DELETE FROM books WHERE id =?", (book_id,))
        CONN.commit()


    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM books")
        books = CURSOR.fetchall()
        return [cls(id=row[0], title=row[1], published_date=row[2], author_id=row[3], available=row[4]) for row in books]


    @classmethod
    def get_by_id(cls, book_id):
        CURSOR.execute("SELECT * FROM books WHERE id =?", (book_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], title=row[1], published_date=row[2], author_id=row[3], available=row[4])
        else:
            return None


