from models.__init__ import CONN, CURSOR
import datetime

class Author:
    def __init__(self, id, name, birth_date):
        self.id = id
        self.name = name
        self.birth_date = birth_date


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Author name must be a string with at least one character.")
        self._name = value

    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("Author birth date must be a valid date.")
        self._birth_date = value
    

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
