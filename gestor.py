from validaciones import validar_nombre, validar_nombre_usuario, validar_numero_entero, normalizar_nombre, validar_hora, fetch_one, fetch_all, ejecutar_consulta
from imprimir import imprimir_tipos_dispositivos, imprimir_dispositivos, imprimir_estados, imprimir_automatizaciones, imprimir_usuarios, imprimir_roles

# Agregar dispositivos

def agregar_dispositivo():
    while True:
        imprimir_dispositivos()
        nombre = validar_nombre(normalizar_nombre(input("Nombre del dispositivo: ")))
        disp_nombre = fetch_one('SELECT 1 FROM Dispositivo WHERE nombre_dispositivo = ?', (nombre,))
        if disp_nombre:
            print(f'El dispositivo {nombre} ya se encuentra registrado')
            continue
        imprimir_tipos_dispositivos()
        tipo_dispositivo_eleccion = validar_numero_entero("Seleccione un tipo de dispositivo (numerico): ")
        #if tipo == '0':
            #tipo_final = validar_nombre("Ingrese en nombre del tipo de dispostivo: ")
            #Completar luego
        tipo_disp = fetch_one('SELECT 1 FROM Tipo_Dispositivo WHERE id_tipo_dispositivo = ?', (tipo_dispositivo_eleccion,))
        if tipo_disp is None:
            print("Seleccion erronea, el tipo debe estar dentro del rango\n")
            continue
        ejecutar_consulta('INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES (?, ?, ?, ?)', (nombre, tipo_dispositivo_eleccion, 2, 0))
        print(f"Dispositivo {nombre} agregado correctamente.\n")
        return

# Modificar Dispositivo

def modificar_dispositivo():
    while True:
        imprimir_dispositivos()
        id_dispositivo = validar_numero_entero('\nIngrese el ID del dispositivo que desea modificar: ')
        dispositivo = fetch_one('SELECT 1 FROM Dispositivo WHERE id_dispositivo = ?', (id_dispositivo,))
        if dispositivo is None:
            print('El dispositivo que intenta seleccionar esta fuera de rango.\n')
            continue
        nuevo_nombre_dispositivo = normalizar_nombre(validar_nombre('\nIngrese el nuevo nombre del dispositivo: '))
        nombre_existente = fetch_one('SELECT 1 FROM Dispositivo WHERE nombre_dispositivo = ?', (nuevo_nombre_dispositivo,))
        if nombre_existente:
            print('El nombre que intenta utilizar ya esta registrado.\n')
            continue
        imprimir_tipos_dispositivos()
        id_tipo_dispositivo = validar_numero_entero('\nIngrese el nuevo tipo de dispositivo (NUMERICO): ')
        tipo_dispositivo = fetch_one('SELECT 1 FROM Tipo_Dispositivo WHERE id_tipo_dispositivo = ?', (id_tipo_dispositivo,))
        if tipo_dispositivo is None:
            print('El tipo que intenta seleccionar se encuentra fuera de rango.\n')
            continue
        imprimir_estados()
        id_estado = validar_numero_entero('\nSeleccione el nuevo estado: ')
        estado = fetch_one('SELECT 1 FROM Estado WHERE id_estado = ?', (id_estado,))
        if estado is None:
            print('El estado que intenta seleccionar se encuentra fuera de rango.\n')
            continue
        ejecutar_consulta('UPDATE Dispositivo SET nombre_dispositivo = ?, id_tipo_dispositivo = ?, id_estado = ? WHERE id_dispositivo = ?', (nuevo_nombre_dispositivo, id_tipo_dispositivo, id_estado, id_dispositivo,))
        print(f"\nDispositivo {nuevo_nombre_dispositivo} modificado correctamente.\n")
        return

# Eliminar dispositivos

def eliminar_dispositivo():
    imprimir_dispositivos()
    id_eleccion = validar_numero_entero('\nIngrese el numero del dispositivo que desee eliminar: ')
    disp = fetch_one('SELECT 1 FROM Dispositivo WHERE id_dispositivo = ?', (id_eleccion,))
    if not disp:
        print('Dispositivo no encontrado. \n')
        return
    confirmacion = validar_numero_entero('Ingrese el ID de nuevo para confirmar: ')
    if confirmacion == id_eleccion:
        ejecutar_consulta('DELETE FROM Dispositivo WHERE id_dispositivo = ?', (id_eleccion,))
        print('Dispositivo eliminado.\n')
    else:
        print('Eliminación cancelada.\n')

# Listar dispositivos

def listar_dispositivos():
    imprimir_dispositivos()

# Buscar dispositivos

def buscar_dispositivo():
    nombre = normalizar_nombre(input('\nIngrese el nombre del dispositivo que desea buscar: ')).strip()
    nombre_dispositivo = fetch_one('SELECT d.id_dispositivo, d.nombre_dispositivo, t.nombre_tipo_dispositivo ' \
    'FROM Dispositivo d JOIN Tipo_Dispositivo t ON d.id_tipo_dispositivo = t.id_tipo_dispositivo WHERE d.nombre_dispositivo = ?', (nombre,))
    if nombre_dispositivo:
        print('-' * 65)
        print(f' {'ID':<5} {'Nombre':<25} {'Tipo':<25}')
        print('-' * 65)           
        print(f'{nombre_dispositivo[0]:<5} {nombre_dispositivo[1]:<25} {nombre_dispositivo[2]:<25}')
        print('-' * 65)
    else:
        print(f"El dispositivo {nombre} no fue hallado\n")

# Agregar automatizaciones

def agregar_automatizacion():
    while True:
        nombre = normalizar_nombre(validar_nombre("Introduzca el nombre de la automatizacion: "))
        nombre_automatizacion = fetch_one('SELECT 1 FROM Automatizacion WHERE nombre_automatizacion = ?', (nombre,))
        if nombre_automatizacion:
            print(f"La automatización {nombre} ya existe.\n")
            continue
        imprimir_dispositivos()
        dispositivo_indice = validar_numero_entero("Seleccione un dispositivo: ")
        id_dispositivo = fetch_one('SELECT 1 FROM Dispositivo WHERE id_dispositivo = ?', (dispositivo_indice,))
        if id_dispositivo is None:
            print("Error: Ingrese uno de los numeros listados que sean validos\n")
            continue
        imprimir_estados()
        estado_eleccion = validar_numero_entero("Seleccione un estado: ")
        estados = fetch_one('SELECT 1 FROM Estado WHERE id_estado = ?', (estado_eleccion,))
        if estados is None:
            print("Error: Ingrese uno de los numeros listados que sean validos\n")
            continue
        hora_inicio = validar_hora("Ingrese el horario el cual debe de iniciar la accion (Use el horario militar, es decir, 8:30PM => 2030): ")
        hora_fin = validar_hora("Ingresar el horario el cual debe de finalizar la accion (Use el horario militar, es decir, 8:30PM => 2030):")
        if hora_inicio == hora_fin:
            print('\nError: La hora de inicio y final no pueden ser iguales, elija una hora final distinta a la hora de inicio.')
            continue
        ejecutar_consulta('INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, id_estado, hora_inicio, hora_fin, activo) VALUES (?, ?, ?, ?, ?, ?)', (nombre, dispositivo_indice, estado_eleccion, hora_inicio, hora_fin, 1))
        print("Automatizacion agregada con exito")
        return

# Modificar automatizaciones

def modificar_automatizacion():
    while True:
        imprimir_automatizaciones()
        auto_eleccion = validar_numero_entero("Ingrese el ID de la automatizacion que desea modificar: ")
        id_automatizacion = fetch_one('SELECT id_automatizacion FROM Automatizacion WHERE id_automatizacion = ?', (auto_eleccion,))
        if id_automatizacion is None:    
            print(f"La automatizacion seleccinada esta fuera de rango no fue hallada.\n")
            continue
        auto = fetch_all('''
        SELECT a.nombre_automatizacion, d.id_dispositivo, a.hora_inicio, a.hora_fin, e.id_estado
        FROM Automatizacion a 
        JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo JOIN Estado e ON a.id_estado = e.id_estado
        WHERE a.id_automatizacion = ?''', (auto_eleccion,))
        print("-" * 130)
        print(f" {'Nombre':<25} {'Dispositivos':<25} {'Hora Inicio':<25} {'Hora Fin':<25} {'Estado'}")
        print("-" * 130)
        fila = auto[0]
        nombre = fila[0]
        dispositivo = fila[1]
        hora_inicio = fila[2]
        hora_fin = fila[3]
        estado = fila[4]
        print(f"{nombre:<25} {dispositivo:<25} {hora_inicio:<25} {hora_fin:<25} {estado}")
        print("-" * 130)
        nueva_hora_inicio = validar_hora("Ingrese el horario que desea que inicie la automatizacion: ")
        nueva_hora_fin = validar_hora("Ingrese el horario que desea que finalice la automatizacion: ")
        if nueva_hora_inicio == nueva_hora_fin:
            print('\nError: La hora de inicio y final no pueden ser iguales, elija una hora final distinta a la hora de inicio.')
            continue
        imprimir_estados()
        nuevo_estado = validar_numero_entero("Seleccione el estado que desea que cambie automaticamente: ")
        estados = fetch_one('SELECT 1 FROM Estado WHERE id_estado = ?', (nuevo_estado,))
        if estados is None:
            print("Error: Ingrese uno de los numeros listados que sean validos\n")
            continue 
        ejecutar_consulta('''
        UPDATE Automatizacion SET id_dispositivo = ?, hora_inicio = ?, hora_fin = ?, id_estado = ?, activo = ?
        WHERE id_automatizacion = ?''', (dispositivo, nueva_hora_inicio, nueva_hora_fin, nuevo_estado, 1, auto_eleccion))
        print(f"La automatizacion {fila[0]} fue actualizada exitosamente\n")
        return


# Eliminar automatizaciones

def eliminar_automatizacion():
    while True:
        imprimir_automatizaciones()
        id_automatizacion = validar_numero_entero("Ingrese el nombre de la automatizacion a eliminar: ")
        automatizacion = fetch_one('SELECT 1 FROM Automatizacion WHERE id_automatizacion = ?', (id_automatizacion))
        if automatizacion is None:
            print(f'La automatizacion {id_automatizacion} no fue hallada.\n')
            continue
        confirmacion = validar_numero_entero('Ingrese el ID de nuevo para confirmar: ')
        if confirmacion == id_automatizacion:
            ejecutar_consulta('DELETE FROM Automatizacion WHERE id_automatizacion = ?', (id_automatizacion))
            print('La automatizacion fue eliminada exitosamente.\n')
        else:
            print('Eliminacion cancelada.\n')
        return

# Listar Automatizaciones

def listar_automatizaciones():
    imprimir_automatizaciones()

# Modificar Rol Usuario

def modificar_rol_usuario():
    while True:
        imprimir_usuarios()
        usuario_eleccion = validar_numero_entero('Ingrese el ID del usuario que desea modificar: ')
        id_usuario = fetch_one('SELECT 1 FROM Usuario WHERE id_usuario = ?', (usuario_eleccion,))
        if id_usuario is None:
            print('El usuario que desea seleccionar se encuentra fuera de rango.\n')
            continue
        imprimir_roles()
        rol_eleccion = validar_numero_entero('Ingrese el ID del rol que desea designarle al usuario: ')
        id_rol = fetch_one('SELECT 1 FROM Rol WHERE id_rol = ?', (rol_eleccion,))
        if id_rol is None:
            print('El rol que desea seleccionar se encuentra fuera de rango.\n')
            continue
        ejecutar_consulta('UPDATE Usuario SET id_rol_usuario = ? WHERE id_usuario = ?', (rol_eleccion, usuario_eleccion,))
        print('El rol del usuario se actualizo con exito.\n')
        return

def buscar_usuario():
    while True:
        nombre = normalizar_nombre(input('Ingrese el nombre del usuario que desea buscar: '))
        nombre_usuario = fetch_one('''
                            SELECT u.id_usuario, u.nombre_usuario, r.nombre_rol
                            FROM Usuario u
                            JOIN Rol r ON u.id_rol_usuario = r.id_rol
                            WHERE nombre_usuario = ?''',  (nombre,))
        if nombre_usuario:
            print('-' * 65)
            print(f' {'ID':<5} {'Nombre':<25} {'Rol':<25}')
            print('-' * 65)           
            print(f'{nombre_usuario[0]:<5} {nombre_usuario[1]:<25} {nombre_usuario[2]:<25}')
            print('-' * 65)
        else:
            print(f"El usuario {nombre} no fue hallado\n")
        return

def listar_usuarios():
    imprimir_usuarios()
    
