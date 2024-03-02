import os
from urllib.parse import quote_plus

class Config:
    server = "tcp:twsoptionscanner.database.windows.net"
    database = os.getenv('DATABASE_NAME')
    username = os.getenv('DATABASE_USERNAME')
    password = os.getenv('DATABASE_PASSWORD')

    driver = '{ODBC Driver 18 for SQL Server}'

    odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
    connect_str = 'mssql+pyodbc:///?odbc_connect=' + quote_plus(odbc_str)

    SQLALCHEMY_DATABASE_URI = connect_str