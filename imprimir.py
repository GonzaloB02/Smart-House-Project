from conexion_base_de_datos import obtener_conexion

def imprimir_dispositivos():
    conn = obtener_conexion()
    cursor = conn.cursor()
    # d = tabla dispositivo | t = tabla tipo dispositivo | e = tabla estado
    cursor.execute('''
        SELECT d.id_dispositivo, d.nombre_dispositivo, t.nombre_tipo_dispositivo, e.nombre_estado  
        FROM Dispositivo d
        JOIN Tipo_Dispositivo t ON d.id_tipo_dispositivo = t.id_tipo_dispositivo
        JOIN Estado e ON d.id_estado = e.id_estado
        ''')
    dispositivos = cursor.fetchall()
    print('-' * 70)
    print(f'{'ID':<5} {'Nombre':<25} {'Tipo':<20} {'Estado':<15}')
    print('-' * 70)
    for disp in dispositivos:
        print(f'{disp.id_dispositivo:<5} {disp.nombre_dispositivo:<25} {disp.nombre_tipo_dispositivo:<20} {disp.nombre_estado:<15}')
        print('-' * 70)
    conn.close()

def imprimir_estados():
    conn = obtener_conexion()
    cursor = conn.cursor()
    # e = tabla estado
    cursor.execute('''
        SELECT e.id_estado, e.nombre_estado
        FROM Estado e
        ''')
    estados = cursor.fetchall()
    print("-" * 35)
    print(f"{'ID':<5} {'Estados':<15}")
    print("-" * 35)
    #print("0. Agregar nuevo estado.")
    for est in estados:
        print(f'{est.id_estado:<5} {est.nombre_estado:<15}')
        print('-' * 35)
    conn.close()

def imprimir_tipos_dispositivos():
    conn = obtener_conexion()
    cursor = conn.cursor()
    # t = tabla tipos dispositivos
    cursor.execute('''
        SELECT t.id_tipo_dispositivo, t.nombre_tipo_dispositivo
        FROM Tipo_Dispositivo t
        ''')
    tipos_dispositivos = cursor.fetchall()
    print("-" * 45)
    print(f" {'ID':<5} {'Tipo':<25}")
    print("-" * 45)
    #print("0. Añadir nuevo tipo dispositivo.")
    for td in tipos_dispositivos:
        print(f'{td.id_tipo_dispositivo:<5} {td.nombre_tipo_dispositivo:<25}')
        print('-' * 45)
    conn.close()

def imprimir_automatizaciones():
    conn = obtener_conexion()
    cursor = conn.cursor()
    # a = tabla automatizaciones | d = tabla dispositivos | e = tabla estados
    cursor.execute('''
        SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, a.hora_inicio, a.hora_fin, e.nombre_estado
        FROM Automatizacion a
        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
        JOIN Estado e ON a.id_estado = e.id_estado
        ''')
    automatizaciones = cursor.fetchall()
    print('-' * 120)
    print(f' {'ID':<5} {'Nombre':<25} {'Dispositivo':<25} {'Hora Inicio':<25} {'hora_fin':<25} {'Estado'}')
    print('-' * 120)
    for auto in automatizaciones:
        print(f'{auto.id_automatizacion:<5} {auto.nombre_automatizacion:<25} {auto.nombre_dispositivo:<25} {str(auto.hora_inicio):<25} {str(auto.hora_fin):<25} {auto.nombre_estado}')
        print('-' * 120)
    conn.close()

def imprimir_usuarios():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT u.id_usuario, u.nombre_usuario, r.nombre_rol
        FROM Usuario u
        JOIN Rol r ON u.id_rol_usuario = r.id_rol
        ''')
    usuarios = cursor.fetchall()
    print('-' * 70)
    print(f' {'ID':<5} {'Nombre':<25} {'Rol':<25}')
    print('-' * 70)
    for u in usuarios:
        print(f' {u.id_usuario:<5} {u.nombre_usuario:<25} {u.nombre_rol:<25}')
        print('-' * 70)
    conn.close()

def imprimir_roles():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT r.id_rol, r.nombre_rol
        FROM Rol r
        ''')
    roles = cursor.fetchall()
    print(f'-' * 45)
    print(f' {'ID':<5} {'Nombre':<25}')
    print(f'-' * 45)
    for r in roles:
        print(f' {r.id_rol:<5} {r.nombre_rol:<25}')
        print('-' * 45)
    conn.close()
