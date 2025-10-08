from conn.conexion_base_de_datos import fetch_one, fetch_all, ejecutar_consulta
from dominio.dispositivo import Dispositivo

class DispositivoDAO:

    def obtener_todo_activo_dispositivo():
        filas = fetch_all('''
                        SELECT d.id_dispositivo, d.nombre_dispositivo, t.nombre_tipo_dispositivo, e.nombre_estado, activo
                        FROM Dispositivo d
                        JOIN Tipo_Dispositivo t ON d.id_tipo_dispositivo = t.id_tipo_dispositivo
                        JOIN Estado e ON d.id_estado = e.id_estado
                        WHERE activo = 1''')
        return [Dispositivo(*fila) for fila in filas] if filas else None
    
    def obtener_id_dispositivo(id_dispositivo):
        filas = fetch_one('''
                        SELECT id_dispositivo, nombre_dispositivo, id_tipo_dispositivo, id_estado
                        FROM Dispositivo
                        WHERE id_dispositivo = ?''', (id_dispositivo,))
        
        return ({'id_dispositivo' : filas[0], 'nombre_dispositivo' : filas[1], 'id_tipo_dispositivo' : filas[2], 'id_estado' : filas[3]}) if filas else None
    
    def buscar_existencia_nombre(nombre):
        fila = fetch_one('''
                        SELECT 1
                        FROM Dispositivo
                        WHERE nombre_dispositivo = ?''', (nombre,))
        return fila if fila else None
    
    def crear_dispositivo(nombre_dispositivo, id_tipo_dispositivo, id_estado=0, activo=1):
        ejecutar_consulta('''
                        INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo)
                        VALUES (?, ?, ?, ?)''',
                        (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo))
        
    def actualizar_dispositivo(dispositivo):
        ejecutar_consulta('''
                        UPDATE Dispositivo SET nombre_dispositivo = ?, id_tipo_dispositivo = ?, id_estado = ?
                        WHERE id_dispositivo = ?''', (dispositivo[0], dispositivo[1], dispositivo[2], dispositivo[3]))
        
    def eliminar_dispositivo(id_dispositivo):
        ejecutar_consulta('''
                        UPDATE Dispositivo 
                        SET activo = 0
                        WHERE id_dispositivo = ?''', (id_dispositivo,))
        
    def re_activar(nombre, tipo_dispositivo_eleccion):
        ejecutar_consulta('''
                        UPDATE Dispositivo
                        SET id_tipo_dispositivo = ?, id_estado = ?, activo = ?
                        WHERE nombre_dispositivo = ?''', (tipo_dispositivo_eleccion, 2, 1, nombre))

    def imprimir_dispositivos_activos():
        fila = DispositivoDAO.obtener_todo_activo_dispositivo()
        print('-' * 70)
        print(f'{'ID':<5} {'Nombre':<25} {'Tipo':<20} {'Estado':<15}')
        print('-' * 70)
        for disp in fila:
            print(f'{disp.id_dispositivo:<5} {disp.nombre_dispositivo:<25} {disp.id_tipo_dispositivo:<20} {disp.id_estado:<15}')
            print('-' * 70)

    def imprimir_dispositivos():
        filas = fetch_all('''
                        SELECT id_dispositivo, nombre_dispositivo
                        FROM Dispositivo''')
        print('-' * 30)
        print(f'{'ID':<5} {'Nombre':<25}')
        print('-' * 30)
        for fila in filas:
            print(f'{fila[0]:<5} {fila[1]:<25}')
            print('-' * 30)
    
    def imprimir_busqueda(nombre):
        filas = fetch_all('''
                        SELECT d.id_dispositivo, d.nombre_dispositivo, t.nombre_tipo_dispositivo, e.nombre_estado
                        FROM Dispositivo d
                        JOIN Tipo_Dispositivo t ON d.id_tipo_dispositivo = t.id_tipo_dispositivo
                        JOIN Estado e ON d.id_estado = e.id_estado
                        WHERE d.nombre_dispositivo = ?''', (nombre,))
        fila = filas[0]
        print('-' * 70)
        print(f'{'ID':<5} {'Nombre':<25} {'Tipo':<20} {'Estado':<15}')
        print('-' * 70)
        print(f'{fila[0]:<5} {fila[1]:<25} {fila[2]:<20} {fila[3]:<15}')
        print('-' * 70)

    def dispositivo_activo(nombre):
        fila = fetch_one('''
                        SELECT activo FROM Dispositivo WHERE nombre_dispositivo = ?''', (nombre,))
        if fila is not None:
            return fila[0]
        else:
            return None

