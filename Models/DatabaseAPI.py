import sqlite3


class DatabaseAPI:
    def __init__(self):
        connection = sqlite3.connect("Models\\CharacterData.db")
        cursor = connection.cursor()

        result = cursor.execute("SELECT name FROM sqlite_master")
        print(result.fetchone())
