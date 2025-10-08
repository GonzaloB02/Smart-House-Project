from conn.conexion_base_de_datos import fetch_one, fetch_all, ejecutar_consulta
from dominio.rol import Rol

class RolDAO:

    def obtener_todos_roles():
        filas = fetch_all('''
                        SELECT id_rol, nombre_rol
                        FROM Rol''')
        return [Rol(*fila) for fila in filas] if filas else None

    def imprimir_roles():
        filas = RolDAO.obtener_todos_roles()
        print(f'-' * 45)
        print(f' {'ID':<5} {'Nombre':<25}')
        print(f'-' * 45)
        for r in filas:
            print(f' {r.id_rol:<5} {r.nombre_rol:<25}')
            print('-' * 45)

    def obtener_id_rol(id_rol):
        fila = fetch_one('''
                        SELECT id_rol, nombre_rol
                        FROM Rol
                        WHERE id_rol = ?''', (id_rol,))
        return ({'id_rol' : fila[0], 'nombre_rol' : fila[1]}) if fila else None
    
