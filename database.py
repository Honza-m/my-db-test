import os, psycopg2, psycopg2.extras
from psycopg2 import sql

class Get:
    def __init__(self, table):
        self.table = table
        DATABASE_URL = os.environ.get('DATABASE_URL')

        self.conn = psycopg2.connect(DATABASE_URL,
                                sslmode='require',
                                cursor_factory=psycopg2.extras.DictCursor)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()
        self.cur.close()

    def get_all(self):
        self.cur.execute("SELECT * FROM {}".format(self.table))
        return self.cur.fetchall()

    def add_one(self, x):
        if not isinstance(x, dict): raise TypeError("Provide x as dict representing one row where dict key is column name and value is row value.")
        self.cur.execute(
            "INSERT INTO {} ({}) VALUES ({})".format(self.table,
                                                     ", ".join([a for a in x.keys()]),
                                                     ", ".join(["%s" for x in range(len(x.values()))])),
            tuple(x.values()))
        self.conn.commit()
