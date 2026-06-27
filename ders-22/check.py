import pyodbc
# Bilgisayarındaki TÜM yüklü ODBC sürücülerini listeler
print([x for x in pyodbc.drivers() if 'SQL Server' in x])