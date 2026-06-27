import pyodbc

from connection import get_connection


def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()


def row_to_dict(cursor: pyodbc.Cursor, row) -> dict:
    columns = [col[0] for col in cursor.description]
    result = {}
    for column, value in zip(columns, row):
        if isinstance(value, str):
            value = value.strip()
        result[column] = value
    return result


def fetchone_dict(cursor: pyodbc.Cursor) -> dict | None:
    row = cursor.fetchone()
    if row is None:
        return None
    return row_to_dict(cursor, row)


def fetchall_dict(cursor: pyodbc.Cursor) -> list[dict]:
    return [row_to_dict(cursor, row) for row in cursor.fetchall()]
