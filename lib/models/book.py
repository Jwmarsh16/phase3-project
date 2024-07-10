from models.__init__ import CONN, CURSOR

class Book:
    def __init__(self, id, title, published_date, author_id, available=True):
        self.id = id
        self.title = title
        self.published_date = published_date
        self.author_id = author_id
        self.available = available


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

