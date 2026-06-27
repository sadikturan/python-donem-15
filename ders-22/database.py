import pyodbc

SERVER = r'.\SQLEXPRESS'
DATABASE = 'Northwind'
DRIVER = '{ODBC Driver 17 for SQL Server}'

CONNECTION_STRING = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'

def get_connection():
    """
    SQL Server'a yeni bir bağlantı açar ve bağlantı nesnesini döner.
    """
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        return conn
    except pyodbc.Error as e:
        print("Veritabanına bağlanılamadı:", e)
        raise e
    
# print([x for x in pyodbc.drivers() if 'SQL Server' in x])

# connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID=sa;PWD=Sifreniz123;'