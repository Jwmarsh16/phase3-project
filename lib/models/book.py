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


    @classmethod
    def create(cls, title, published_date, author_id):

        pass

    @classmethod
    def delete(cls, book_id):

        pass

    @classmethod
    def get_all(cls):

        pass

    @classmethod
    def get_by_id(cls, book_id):

        pass

