from validaciones import normalizar_nombre, validar_nombre_usuario, validar_contraseña_usuario, introducir_opcion, introducir_opcion_2, introducir_opcion_3, introducir_opcion_4, registrar_usuario, comparar_usuario, CONSTANTS_ROLES
from gestor import agregar_dispositivo, modificar_dispositivo, buscar_dispositivo, eliminar_dispositivo, listar_dispositivos, agregar_automatizacion, modificar_automatizacion, eliminar_automatizacion, listar_automatizaciones, modificar_rol_usuario, buscar_usuario, listar_usuarios

# Menu Puente

def menu_intermedio(msg, login, menu_dispositivos, menu_automatizaciones, menu_rol):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion(opcion):
            print("Error: Opcion no valida, ingrese un numero dentro del rango indicado\n")
            continue
        if opcion == '1': 
            login = True
            menu_dispositivos = True
            menu_automatizaciones = False
            menu_rol = False
            return login, menu_dispositivos, menu_automatizaciones, menu_rol
        if opcion == '2':
            login = True
            menu_dispositivos = False
            menu_automatizaciones = True
            menu_rol = False
            return login, menu_dispositivos, menu_automatizaciones, menu_rol
        if opcion == '9':
            login = True
            menu_dispositivos = False
            menu_automatizaciones = False
            menu_rol = True
            return login, menu_dispositivos, menu_automatizaciones, menu_rol
        if opcion == '0':
            login = False
            menu_dispositivos = False
            menu_automatizaciones = False
            menu_rol = False
            return login, menu_dispositivos, menu_automatizaciones, menu_rol

# Menu Dispositivos

def manipular_dispositivos(msg, usuario, menu_dispositivos):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_2(opcion):
            print("Error: Opcion no valida, ingrese un numero dentro del rango indicado\n")
            continue
        if opcion == '1' and usuario[2] != CONSTANTS_ROLES['INVITADO']:
            agregar_dispositivo()
        elif opcion == '2' and usuario[2] != CONSTANTS_ROLES['INVITADO']:
            modificar_dispositivo()
        elif opcion == '3' and usuario[2] == CONSTANTS_ROLES['ADMIN']:
            eliminar_dispositivo()
        elif opcion == '4':
            listar_dispositivos()
        elif opcion == '5':
            buscar_dispositivo()
        elif opcion == '0':
            menu_dispositivos = False
            return usuario, menu_dispositivos
        else:
            print('No posee permisos para utilizar esta opcion.\n')

# Menu Automatizaciones

def manipular_automatizaciones(msg, usuario, menu_automatizaciones):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_3(opcion):
            print("Error: Opcion no valida, ingrese un numero dentro del rango indicado\n")
            continue
        elif opcion == '1' and usuario[2] != CONSTANTS_ROLES['INVITADO']:
            agregar_automatizacion()
        elif opcion == '2' and usuario[2] != CONSTANTS_ROLES['INVITADO']:
            modificar_automatizacion()
        elif opcion == '3' and usuario[2] == CONSTANTS_ROLES['ADMIN']:
            eliminar_automatizacion()
        elif opcion == '4':
            listar_automatizaciones()
        elif opcion == '0':
            menu_automatizaciones = False
            return usuario, menu_automatizaciones
        else:
            print('No posee permisos para utilizar esta opcion.\n')

def manipular_roles(msg, usuario, menu_rol):
    if usuario[2] != CONSTANTS_ROLES['ADMIN']:
        print('No posee permisos para utilizar esta opcion.\n')
        menu_rol = False
        return usuario, menu_rol
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_4(opcion):
            print("Error: Opcion no valida, ingrese un numero dentro del rango indicado\n")
            continue
        elif opcion == '1':
            modificar_rol_usuario()
            return usuario, menu_rol
        elif opcion == '2':
            buscar_usuario()
            return usuario, menu_rol
        elif opcion == '3':
            listar_usuarios()
            return usuario, menu_rol
        elif opcion == '0':
            menu_rol = False
            return usuario, menu_rol

# Menu Login

def menu_login(msg, login, exit, usuario):
    while True:
        codigo = input(msg).strip()

        match codigo:

            case '1':
                nombre = normalizar_nombre(input("\nIngrese el nombre de usuario (minimo 3 caracteres): "))
                contraseña = input("\nIngrese la contraseña (minimo 8 caracteres): ")

                if not validar_nombre_usuario(nombre):
                    print(f"\nEl nombre '{nombre}' no es valido, recuerde que debe ser mayor a 3 caracteres y solo puede utilizar los simbolos (. - _).")
                    continue

                if not validar_contraseña_usuario(contraseña):
                    print(f"\nLa contraseña no es valida, recuerde que debe ser entre 8-15 caracteres y solo puede utilizar los simbolos (. - _).")
                    continue

                eleccion, usuario = comparar_usuario(nombre, contraseña, usuario)
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
                
                if not registrar_usuario(nombre, contraseña):
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