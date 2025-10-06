from conn.conexion_base_de_datos import fetch_one, fetch_all, ejecutar_consulta
from dominio.estado import Estado

class EstadoDAO:

    def obtener_estados():
        filas = fetch_all('''
                        SELECT id_estado, nombre_estado
                        FROM Estado ''')
        return [Estado(*fila) for fila in filas]
    
    def obtener_id_estado(id_estado):
        fila = fetch_one('''
                        SELECT id_estado, nombre_estado
                        FROM Estado
                        WHERE id_estado = ?''', (id_estado,))
        
        return Estado(fila[0], fila[1])

    def imprimir_estados():
        fila = EstadoDAO.obtener_estados()
        print("-" * 35)
        print(f"{'ID':<5} {'Estados':<15}")
        print("-" * 35)
        for est in fila:
            print(f'{est.id_estado:<5} {est.nombre_estado:<15}')
            print('-' * 35)