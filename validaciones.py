import bcrypt
from sistema import Roles, Usuarios, usuarios_registro

def validar_nombre(msg):
    while True:
        valor = input(msg).lower().strip()
        if all(char.isalpha() or char.isspace() for char in valor):
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
    if nombre.isalnum() and len(nombre) >= 3:
        return True
    else:
        return False
    
def validar_contraseña_usuario(contraseña):
    contraseña = contraseña.strip()
    if all(not char.isspace() for char in contraseña) and 15 >= len(contraseña) >= 8:
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
        if valor.isdigit() and 4 > int(valor) >= 0:
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


#
##
### CONTROL DE USUARIOS
##
#

def registrar_usuario(nombre, contraseña):
    if not usuarios_registro:
        rol = Roles.ADMIN
    else:
        rol = Roles.USUARIO
    contraseña_hashed = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
    usuario = Usuarios(nombre, contraseña_hashed, rol)
    usuarios_registro.append(usuario)

def comparar_usuario(nombre, contraseña):
    for usuario in usuarios_registro:
        if usuario.nombre == nombre:
            if bcrypt.checkpw(contraseña.encode(), usuario.contraseña):
                return "acceso"
            return "contraseña_error"
    return "usuario_error"