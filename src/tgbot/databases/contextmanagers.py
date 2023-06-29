import sqlite3 as sq
from contextlib import contextmanager


@contextmanager
def database_connection(db_name: str):
    conn = sq.connect(db_name)
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        conn.close()
