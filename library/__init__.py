import sqlite3

CONN = sqlite3.connect('db/library_management.db')
CURSOR = CONN.cursor()
