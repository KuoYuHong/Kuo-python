import pyodbc
import pandas as pd

server = 'localhost'
database = '{DB_NAME}'
driver = '{ODBC Driver 17 for SQL Server}'
Trusted_Connection = 'yes'
connectionString = 'DRIVER={0};PORT=1433;SERVER={1};DATABASE={2};Trusted_Connection={3}'.format(driver, server, database,Trusted_Connection)
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
Var = ""
Var = pd.read_sql(Var, cnxn)
cnxn.close()

print("Var:",Var)
print("ok")