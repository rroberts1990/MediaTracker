import sqlite3
from sqlite3 import Error
from config_files.sql_templates import sql_templates

class DatabaseManager:
    """Manage interaction with media database in sqllite."""
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns

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
        conn, cursor = self.connect_sqllite()
        cursor.execute(sql_templates["create_table"])

