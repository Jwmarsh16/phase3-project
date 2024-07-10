from models.__init__ import CONN, CURSOR

class Author:
    def __init__(self, id, name, birth_date):
        self.id = id
        self.name = name
        self.birth_date = birth_date

    @classmethod
    def create(cls, name, birth_date):

        pass

    @classmethod
    def delete(cls, author_id):

        pass

    @classmethod
    def get_all(cls):

        pass

    @classmethod
    def get_by_id(cls, author_id):

        pass
