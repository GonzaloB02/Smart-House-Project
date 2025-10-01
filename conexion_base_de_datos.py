import pyodbc

def obtener_conexion():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=SmartHouse;'
        'UID=Python_Admin;'
        'PWD=GBarbuto_02;'
        'TrustServerCertificate=yes;'
    )

