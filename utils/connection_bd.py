import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pydba import PostgresDB

class connection_bd():
    def __init__(self, db="postgres", user="postgres", password="postgres", host='localhost'):
        self.conn = psycopg2.connect(database=db, user=user, password=password)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def fetch_all(self, query):
        self.cur.execute(query)
        self.conn.commit()
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()