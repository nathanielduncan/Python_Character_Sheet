import sqlite3


class DatabaseAPI:
    def __init__(self):
        self.connection = sqlite3.connect("Models\\CharacterData.db")
        self.cursor = self.connection.cursor()

    def dict_factory(self, cursor, row):
        fields = [column[0] for column in cursor.description]
        results_dict = {key: value for key, value in zip(fields, row)}

        for key in results_dict:
            if results_dict[key] is None:
                results_dict[key] = ""

        return results_dict

    def load_character(self, character_name):
        sql_string = "SELECT * FROM Character WHERE Name=\"" + character_name + "\""
        results = self.cursor.execute(sql_string)
        return self.dict_factory(self.cursor, results.fetchone())

