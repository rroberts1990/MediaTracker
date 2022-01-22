import sqlite3
from sqlite3 import Error
from config_files.sql_templates import sql_templates

class DatabaseManager:
    """Manage interaction with media database in sqllite."""
    def __init__(self, name, columns, column_types):
        self.name = name
        self.columns = columns
        self.column_types = column_types
        self.conn, self.cursor = self.connect_sqllite()

    def connect_sqllite(self):
        """create connection to sqllite database"""
        conn = None
        try:
            conn = sqlite3.connect(self.name)
        except Error as e:
            print(e)
        cursor = conn.cursor()
        return conn, cursor

    def create_table(self):
        self.cursor.execute(sql_templates["create_table"])

    def insert_record(self, values):
        insert_statement = sql_templates["insert_record"].format(
            *self.columns, *values)
        self.cursor.execute(insert_statement)


