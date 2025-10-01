import bcrypt
from conexion_base_de_datos import obtener_conexion

CONSTANTS_ROLES = {
            'ADMIN' : 1,
            'USUARIO' : 2,
            'INVITADO' : 3}

def validar_nombre(msg):
    while True:
        valor = input(msg).lower().strip()
        if all(char.replace('_', '').isalpha() or char.isspace() for char in valor):
            return valor
        print("\nNombre no valido, recuerde que los simbolos no son validos.")
        eleccion = input("\n¿Desea cancelar la accion? (SI/NO): ").lower()
        if eleccion == 'si':
            return
        if eleccion == 'no':
            continue
        else:
            print("Error: Eleccion no identificada, recuerde que debe poner 'SI' o 'NO': ")

def validar_numero_entero(msg):
    while True:
        numero = input(msg)
        if numero.isdigit() and int(numero) > 0:
            return int(numero)
        print("Ingrese un numero valido, no debe contener decimales ni simbolos\n")

def validar_numero_flotante(msg):
    while True:
        numero = input(msg)
        if numero.count(".") and numero.replace('.', '').isdigit() <= 1 and int(numero) > 0:
            return float(numero)
        print("Ingrese un numero valido, no debe contener simbolos\n")

def validar_nombre_usuario(nombre):
    nombre = nombre.strip()
    if nombre.replace('_', '').isalnum() and len(nombre) >= 3:
        return True
    else:
        return False
    
def validar_contraseña_usuario(contraseña):
    contraseña = contraseña.strip()
    if all(not char.replace('_', '').isspace() for char in contraseña) and 20 >= len(contraseña) >= 8:
        return True
    else:
        return False
    
def validar_nombre_dispositivo(nombre_dispositivo):
    for char in ".-_":
        nombre_dispositivo = nombre_dispositivo.replace(char, " ")
    if all(char.isspace() or char.isalnum() for char in nombre_dispositivo): 
        return True
    else:
        return False

def validar_hora(msg):
    while True:
        numero = input(msg).strip()

        if len(numero) != 4 or not numero.isdigit():
            print(f"El numero {numero} debe de tener 4 digitos para poder calcularlo\n") 
            continue

        hora = int(numero[:2])
        minutos = int(numero[2:])
        if not (0 <= hora <= 23):
            print(f"Hora fuera del rango (0-23)")
            continue
        if not (0 <= minutos < 60):
            print(f"Minutos fuera del rango (0-60)")
            continue
        if hora == 0:
            return (f"12:{minutos:02d} AM")
        elif hora < 12:
            return (f"{hora:02d}:{minutos:02d} AM")
        elif hora == 12:
            return (f"12:{minutos:02d} PM")
        else:
            return (f"{hora - 12:02d}:{minutos:02d} PM")
#
##
### NORMALIZACIONES
##
#

def normalizar_nombre(nombre):
    return nombre.replace(' ', '_')

#
##
### VALIDACIONES DE ENTRADAS DE LOS MENU'S
##
#

def introducir_opcion(valor):
        if valor.isdigit() and 4 > int(valor) >= 0 or int(valor) == 9:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False

def introducir_opcion_2(valor): 
        if valor.isdigit() and 6 > int(valor) >= 0:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False

def introducir_opcion_3(valor):
        if valor.isdigit() and 5 > int(valor) >= 0:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False

def introducir_opcion_4(valor):
        if valor.isdigit() and 4 > int(valor) >= 0:
            return True
        print("Opcion no valida, por favor ingrese un numero dentro del rango indicado.\n")
        return False


#
##
### CONTROL DE USUARIOS
##
#

def registrar_usuario(nombre, contraseña):
    usuario_existente = fetch_one('SELECT 1 FROM Usuario WHERE nombre_usuario = ?', (nombre,))
    usuario_rol = fetch_all('SELECT id_rol FROM Rol')
    if usuario_existente:
        print('Usuario ya registrado.\n')
        return
    usuarios_totales = fetch_one('SELECT COUNT(*) FROM Usuario')[0]
    rol = usuario_rol[0][0] if usuarios_totales == 0 else usuario_rol[2][0]
    contraseña_hashed = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
    ejecutar_consulta('INSERT INTO Usuario (nombre_usuario, contrasena_usuario, id_rol_usuario) VALUES (?, ?, ?)', (nombre, contraseña_hashed.decode('utf-8'), rol))
    print(f'Usuario {nombre} registrado correctamente con el rol {rol}.\n')

def comparar_usuario(nombre, contraseña, usuario):
    usuario = fetch_one('SELECT contrasena_usuario, id_rol_usuario FROM Usuario WHERE nombre_usuario = ?', (nombre))
    if usuario is None:
        return 'usuario_error', None
    contraseña_guardada, rol = usuario
    if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_guardada.encode('utf-8')):
        usuario = (nombre, contraseña, rol)
        return 'acceso', usuario
    else:
        return 'contraseña_error', None

#
##
### BASE DE DATOS
##
#

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

def ejecutar_consulta(consulta, parametros=()):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(consulta, parametros)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Error al ejecutar la consulta: {e}')