from interfaces.validaciones import validar_nombre_usuario, validar_contraseña_usuario
from interfaces.gestor import agregar_dispositivo, modificar_dispositivo, buscar_dispositivo, eliminar_dispositivo, listar_dispositivos, agregar_automatizacion, modificar_automatizacion, eliminar_automatizacion, listar_automatizaciones, buscar_automatizacion, modificar_rol_usuario, buscar_usuario, listar_usuarios
from dao.usuarioDAO import UsuarioDAO


CONSTANTS_ROLES = {
    'ADMIN' : 1,
    'USUARIO' : 2,
    'INVITADO' : 3
}

# Menu Puente

def menu_intermedio(msg, login, menu_dispositivos, menu_automatizaciones, menu_rol):
    while True:
        codigo = input(msg).strip()
        opciones = {
            '0' : (False, False, False, False),
            '1' : (True, True, False, False),
            '2' : (True, False, True, False),
            '9' : (True, False, False, True)
        }

        if codigo in opciones:
            return opciones[codigo]
        else:
             print("Error: Opcion no valida, ingrese un numero dentro del rango indicado\n")

# Menu Dispositivos

def manipular_dispositivos(msg, usuario, menu_dispositivos):
    while True:
        codigo = input(msg).strip()
        if codigo == '0':
            return usuario, False
        
        opciones = {
            '1' : (CONSTANTS_ROLES['USUARIO'], agregar_dispositivo),
            '2' : (CONSTANTS_ROLES['USUARIO'], modificar_dispositivo),
            '3' : (CONSTANTS_ROLES['ADMIN'], eliminar_dispositivo),
            '4' : (None, listar_dispositivos),
            '5' : (None, buscar_dispositivo)
        }

        if codigo in opciones:
            rol, funcion = opciones[codigo]

            if rol and usuario[2] > rol:
                print('No posee permisos para utilizar esta opcion.\n')
            else:
                funcion()

# Menu Automatizaciones

def manipular_automatizaciones(msg, usuario, menu_automatizaciones):
    while True:

        codigo = input(msg).strip()
        if codigo == '0':
            return usuario, False
        
        opciones = {
            '1' : (CONSTANTS_ROLES['USUARIO'], agregar_automatizacion),
            '2' : (CONSTANTS_ROLES['USUARIO'], modificar_automatizacion),
            '3' : (CONSTANTS_ROLES['ADMIN'], eliminar_automatizacion),
            '4' : (None, listar_automatizaciones),
            '5' : (None, buscar_automatizacion)
        }

        if codigo in opciones:
            rol, funcion = opciones[codigo]

            if rol and usuario[2] > rol:
                print('No posee permisos para utilizar esta opcion.\n')
            else:
                funcion()

def manipular_roles(msg, usuario, menu_rol):

    while True:

        codigo = input(msg).strip()
        if codigo == '0':
            return usuario, False
        
        opciones = {
            '1' : (CONSTANTS_ROLES['ADMIN'], modificar_rol_usuario),
            '2' : (CONSTANTS_ROLES['ADMIN'], buscar_usuario),
            '3' : (CONSTANTS_ROLES['ADMIN'], listar_usuarios),
        }

        if codigo in opciones:
            rol, funcion = opciones[codigo]

            if usuario[2] > rol:
                print('No posee permisos para utilizar esta opcion.\n')
            else:
                funcion()

# Menu Login

def menu_login(msg, login, exit, usuario):
    while True:
        codigo = input(msg).strip()

        match codigo:

            case '1':
                nombre = input("\nIngrese el nombre de usuario (minimo 3 caracteres): ")
                contraseña = input("\nIngrese la contraseña (minimo 8 caracteres): ")

                eleccion, usuario = UsuarioDAO.comparar_usuario(usuario = (nombre, contraseña))
                match eleccion:
                    case "acceso":
                        print("Usuario logeado con exito.\n")
                        login = True
                        exit = False
                        return login, exit, usuario
                    case "contraseña_error":
                        print("Error: Contraseña incorrecta\n")
                        login = False
                        exit = False
                        return login, exit, None
                    case "usuario_error":
                        print("Error: Usuario no registrado\n")
                        login = False
                        exit = False
                        return login, exit, None
                
            case '2':
                nombre = input("Ingrese el nombre de usuario (minimo 3 caracteres): ")
                contraseña = input("Ingrese la contraseña (minimo 8 caracteres): ")
                if not validar_nombre_usuario(nombre):
                    print(f"El nombre {nombre} no es valido, recuerde que solo puede utilizar los simbolos (. - _)\n")
                    continue

                if not validar_contraseña_usuario(contraseña):
                    print(f"La contraseña no es valida, recuerde que solo puede utilizar los simbolos (. - _)\n")
                    continue
                
                if not UsuarioDAO.registrar_usuario(nombre, contraseña):
                    print("Error: El usuario ya se encuentra registrado.\n")
                    login = False
                    exit = False
                    continue
                else:
                    login = False
                    exit = False
                    return login, exit, None
                        
            case '0':
                login = False
                exit = True
                return login, exit, usuario
                
            case _:
                print("Error: El codigo es erroneo, asegurese de no poner letras ni simbolos, solo numeros\n")