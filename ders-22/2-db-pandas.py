import pandas as pd
import pyodbc

SERVER = r'.\SQLEXPRESS'
DATABASE = 'Northwind'
DRIVER = '{ODBC Driver 17 for SQL Server}'

CONNECTION_STRING = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'

conn = pyodbc.connect(CONNECTION_STRING)
df = pd.read_sql("SELECT * FROM Products", conn)
conn.close()

print(df.head())