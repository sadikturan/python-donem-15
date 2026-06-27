import pyodbc

SERVER = r".\SQLEXPRESS"
DATABASE = "Northwind"
DRIVER = "{ODBC Driver 17 for SQL Server}"
# print([x for x in pyodbc.drivers() if 'SQL Server' in x])

CONNECTION_STRING = (
    f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
)


def get_connection() -> pyodbc.Connection:
    return pyodbc.connect(CONNECTION_STRING)
