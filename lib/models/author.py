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

    def save(self):
        if self.id is None:
            CURSOR.execute("INSERT INTO authors (name, birth_date) VALUES (?,?)", (self.name, self.birth_date))
            self.id = CONN.lastrowid
        else:
            CURSOR.execute("UPDATE authors SET name =?, birth_date =? WHERE id =?", (self.name, self.birth_date, self.id))
            CONN.commit()
    

    @classmethod
    def create(cls, name, birth_date):
        author = cls(name=name, birth_date=birth_date)
        author.save()
        return author


    @classmethod
    def delete(cls, author_id):
        CURSOR.execute("DELETE FROM authors WHERE id =?", (author_id,))
        CONN.commit()


    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM authors")
        authors = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], birth_date=row[2]) for row in authors]


    @classmethod
    def get_by_id(cls, author_id):
        CURSOR.execute("SELECT * FROM authors WHERE id =?", (author_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], birth_date=row[2])
        else:
            return None
        
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                birth_date DATE NOT NULL
            )
        """)
        CONN.commit()

