from conn.conexion_base_de_datos import fetch_one, fetch_all
from dominio.tipo_dispositivo import Tipo_Dispositivo

class Tipo_DispositivoDAO:

    def obtener_tipos_dispositivos():
        filas = fetch_all('''
                        SELECT id_tipo_dispositivo, nombre_tipo_dispositivo
                        FROM Tipo_Dispositivo ''')
        return [Tipo_Dispositivo(*fila) for fila in filas] if filas else None

    def obtener_id_tipo_dispositivo(id_tipo_dispositivo):
            filas = fetch_one('''
                            SELECT id_tipo_dispositivo, nombre_tipo_dispositivo
                            FROM Tipo_Dispositivo
                            WHERE id_tipo_dispositivo = ?''', (id_tipo_dispositivo,))
            
            return ({'id_tipo_dispositivo' : filas[0], 'nombre_tipo_dispositivo' : filas[1]}) if filas else None

    def imprimir_tipos_dispositivos():
        fila = Tipo_DispositivoDAO.obtener_tipos_dispositivos()
        print("-" * 45)
        print(f" {'ID':<5} {'Tipo':<25}")
        print("-" * 45)
        #print("0. Añadir nuevo tipo dispositivo.")
        for td in fila:
            print(f'{td.id_tipo_dispositivo:<5} {td.nombre_tipo_dispositivo:<25}')
            print('-' * 45)