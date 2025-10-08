from conn.conexion_base_de_datos import fetch_one, fetch_all, ejecutar_consulta
from dominio.automatizacion import Automatizacion

class AutomatizacionDAO:

    def obtener_todo_activo_automatizacion():
        filas = fetch_all('''
                        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, a.hora_inicio, a.hora_fin, e.nombre_estado, a.activo
                        FROM Automatizacion a
                        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
                        JOIN Estado e ON a.id_estado = e.id_estado
                        WHERE a.activo = 1''')
        return [Automatizacion(*fila) for fila in filas] if filas else None

    def obtener_id_automatizacion(id_automatizacion):
        fila = fetch_one('''
                        SELECT id_automatizacion, nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado
                        FROM Automatizacion
                        WHERE id_automatizacion = ?''', (id_automatizacion,))
        return ({'id_automatizacion' : fila[0], 'nombre_automatizacion' : fila[1], 'id_dispositivo' : fila[2], 'hora_inicio' : fila[3], 'hora_fin' : fila[4], 'id_estado' : fila[5]}) if fila else None

    def buscar_existencia_nombre(nombre_automatizacion):
        fila = fetch_one('''
                        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, a.hora_inicio, a.hora_fin, e.nombre_estado
                        FROM Automatizacion a
                        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
                        JOIN Estado e ON a.id_estado = e.id_estado
                        WHERE nombre_automatizacion = ?''', (nombre_automatizacion,))
        return ({'id_automatizacion' : fila[0], 'nombre_automatizacion' : fila[1], 'id_dispositivo' : fila[2], 'hora_inicio' : fila[3], 'hora_fin' : fila[4], 'id_estado' : fila[5]}) if fila else None

    def obtener_automatizacion(id_automatizacion):
        filas = fetch_all('''
                        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, a.hora_inicio, a.hora_fin, e.nombre_estado, a.activo
                        FROM Automatizacion a
                        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
                        JOIN Estado e ON a.id_estado = e.id_estado
                        WHERE a.id_automatizacion = ?''', (id_automatizacion,))
        return [Automatizacion(*fila) for fila in filas] if filas else None

    def crear_automatizacion(nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado):
        ejecutar_consulta('''
                        INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo)
                        VALUES (?, ?, ?, ?, ?, 1)''',
                        (nombre_automatizacion, id_dispositivo,hora_inicio, hora_fin, id_estado,))

    def actualizar_automatizacion(id_automatizacion, id_estado, hora_inicio, hora_fin):
        ejecutar_consulta('''
                        UPDATE Automatizacion SET id_estado = ?, hora_inicio = ?, hora_fin = ?
                        WHERE id_automatizacion = ?''', (id_estado, hora_inicio, hora_fin, id_automatizacion,))

    def eliminar_automatizacion(id_automatizacion):
        ejecutar_consulta('''
                        UPDATE Automatizacion SET activo = ?
                        WHERE id_automatizacion = ?''', (0, id_automatizacion,))

    def re_activar_automatizacion(nombre_automatizacion, dispositivo_indice, hora_inicio, hora_fin, estado_eleccion):
        ejecutar_consulta('''
                        UPDATE Automatizacion SET id_dispositivo = ?, hora_inicio = ?, hora_fin = ?, id_estado = ?, activo = 1
                        WHERE nombre_automatizacion = ?''', (dispositivo_indice, hora_inicio, hora_fin, estado_eleccion, nombre_automatizacion,))
    
    def imprimir_automatizaciones():
        fila = AutomatizacionDAO.obtener_todo_activo_automatizacion()
        print('-' * 130)
        print(f' {'ID':<5} {'Nombre':<25} {'Dispositivo':<25} {'Hora Inicio':<25} {'hora_fin':<25} {'Estado'}')
        print('-' * 130)
        for auto in fila:
            print(f'{auto.id_automatizacion:<5} {auto.nombre_automatizacion:<25} {auto.id_dispositivo:<25} {str(auto.hora_inicio):<25} {str(auto.hora_fin):<25} {auto.id_estado}')
            print('-' * 130)

    def imprimir_busqueda(nombre):
        filas = fetch_all('''
                        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, a.hora_inicio, a.hora_fin, e.nombre_estado, a.activo
                        FROM Automatizacion a
                        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
                        JOIN Estado e ON a.id_estado = e.id_estado
                        WHERE a.nombre_automatizacion = ?''', (nombre,))
        fila = filas[0]
        print('-' * 130)
        print(f' {'ID':<5} {'Nombre':<25} {'Dispositivo':<25} {'Hora Inicio':<25} {'hora_fin':<25} {'Estado'}')
        print('-' * 130)
        print(f'{fila[0]:<5} {fila[1]:<25} {fila[2]:<25} {str(fila[3]):<25} {str(fila[4]):<25} {fila[5]}')
        print('-' * 130)

    def automatizacion_activa(nombre):
        fila = fetch_one('''
                        SELECT activo FROM Automatizacion WHERE nombre_automatizacion = ?''', (nombre,))
        if fila is not None:
            return fila[0]
        else:
            return None

