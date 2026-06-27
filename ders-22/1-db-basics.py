import pyodbc

SERVER = r'.\SQLEXPRESS'
DATABASE = 'Northwind'
DRIVER = '{ODBC Driver 17 for SQL Server}'
# print([x for x in pyodbc.drivers() if 'SQL Server' in x])

CONNECTION_STRING = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
# connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID=sa;PWD=Sifreniz123;'

conn = pyodbc.connect(CONNECTION_STRING)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Products")
for row in cursor.fetchall():
    print(row.ProductName, row.UnitPrice)

conn.close()