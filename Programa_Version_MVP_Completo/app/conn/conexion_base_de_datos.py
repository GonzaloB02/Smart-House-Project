import pyodbc
def obtener_conexion():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=SmartHouse;'
        'UID= - ;'
        'PWD= - ;'
        'TrustServerCertificate=yes;'
    )

def fetch_one(consulta, parametros=()):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        fila = cursor.fetchone()
        conn.close()
        return fila
    except Exception as e:
        print(f'Error al ejecutar la consulta: {e}')
        return []

def fetch_all(consulta, parametros=()):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        fila = cursor.fetchall()
        conn.close()
        return fila
    except Exception as e:
        print(f'Error al ejecutar la consulta: {e}')
        return []

def ejecutar_consulta(consulta, parametros=()):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error al ejecutar la consulta: {e}')

        return []
