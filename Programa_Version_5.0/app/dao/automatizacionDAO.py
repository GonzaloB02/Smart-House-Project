from conn.conexion_base_de_datos import fetch_one, fetch_all, ejecutar_consulta
from dominio.automatizacion import Automatizacion

class AutomatizacionDAO:

    def obtener_todo_activo_automatizacion():
        filas = fetch_all('''
                        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, e.nombre_estado, a.hora_inicio, a.hora_fin, a.activo
                        FROM Automatizacion a
                        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
                        JOIN Estado e ON a.id_estado = e.id_estado
                        WHERE a.activo = 1''')
        return [Automatizacion(*fila) for fila in filas]

    def obtener_id_automatizacion(id_automatizacion):
        fila = fetch_one('''
                        SELECT id_automatizacion, nombre_automatizacion, id_dispositivo, id_estado, hora_inicio, hora_fin, activo
                        FROM Automatizacion
                        WHERE id_automatizacion = ?''', (id_automatizacion,))
        return Automatizacion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

    def buscar_existencia_nombre(nombre_automatizacion):
        fila = fetch_one('''
                        SELECT 1 
                        FROM Automatizacion
                        WHERE nombre_automatizacion = ?''', (nombre_automatizacion,))
        return fila is not None

    def obtener_automatizacion(id_automatizacion):
        filas = fetch_all('''
                        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, a.hora_inicio, a.hora_fin, e.nombre_estado, a.activo
                        FROM Automatizacion a
                        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
                        JOIN Estado e ON a.id_estado = e.id_estado
                        WHERE a.id_automatizacion = ?''', (id_automatizacion,))
        return [Automatizacion(*fila) for fila in filas]

    def crear_automatizacion(nombre_automatizacion, id_dispositivo, id_estado, hora_inicio, hora_fin, activo=1):
        ejecutar_consulta('''
                        INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, id_estado, hora_inicio, hora_fin, activo)
                        VALUES (?, ?, ?, ?, ?, ?)''',
                        (nombre_automatizacion, id_dispositivo, id_estado, hora_inicio, hora_fin, activo,))

    def actualizar_automatizacion(id_automatizacion, id_estado, hora_inicio, hora_fin):
        ejecutar_consulta('''
                        UPDATE Automatizacion SET id_estado = ?, hora_inicio = ?, hora_fin = ?
                        WHERE id_automatizacion = ?''', (id_estado, hora_inicio, hora_fin, id_automatizacion,))

    def eliminar_automatizacion(id_automatizacion):
        ejecutar_consulta('''
                        UPDATE Automatizacion SET activo = ?
                        WHERE id_automatizacion = ?''', (0, id_automatizacion,))

    def re_activar_automatizacion(nombre_automatizacion):
        ejecutar_consulta('''
                        UPDATE Automatizacion SET id_estado = ?, activo = ?
                        WHERE nombre_automatizacion = ?''', (2, 1, nombre_automatizacion,))
    
    def imprimir_automatizaciones():
        fila = AutomatizacionDAO.obtener_todo_activo_automatizacion()
        print('-' * 130)
        print(f' {'ID':<5} {'Nombre':<25} {'Dispositivo':<25} {'Hora Inicio':<25} {'hora_fin':<25} {'Estado'}')
        print('-' * 130)
        for auto in fila:
            print(f'{auto.id_automatizacion:<5} {auto.nombre_automatizacion:<25} {auto.id_dispositivo:<25} {str(auto.hora_inicio):<25} {str(auto.hora_fin):<25} {auto.id_estado}')
            print('-' * 130)

    def automatizacion_activa(nombre):
        fila = fetch_one('''
                        SELECT activo FROM Automatizacion WHERE nombre_automatizacion = ?''', (nombre,))
        return fila

