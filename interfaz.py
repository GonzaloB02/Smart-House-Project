from validaciones import validar_nombre_usuario, validar_contraseña_usuario, introducir_opcion, introducir_opcion_2, introducir_opcion_3, registrar_usuario, comparar_usuario
from gestor import agregar_dispositivo, modificar_dispositivo, buscar_dispositivo, eliminar_dispositivo, listar_dispositivos, agregar_automatizacion, modificar_automatizacion, eliminar_automatizacion, listar_automatizaciones

# Menu Puente

def menu_intermedio(msg, login, menu_dispositivos, menu_automatizaciones):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion(opcion):
            print("Error: Opcion no valida, ingrese un numero dentro del rango indicado\n")
            continue
        if opcion == '1': 
            login = True
            menu_dispositivos = True
            menu_automatizaciones = False
            return login, menu_dispositivos, menu_automatizaciones
        if opcion == '2':
            login = True
            menu_dispositivos = False
            menu_automatizaciones = True
            return login, menu_dispositivos, menu_automatizaciones
        if opcion == '0':
            login = False
            menu_dispositivos = False
            menu_automatizaciones = False
            return login, menu_dispositivos, menu_automatizaciones 

# Menu Dispositivos

def manipular_dispositivos(msg, menu_dispositivos):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_2(opcion):
            continue
        if opcion == '1':
            agregar_dispositivo()
        elif opcion == '2':
            modificar_dispositivo()
        elif opcion == '3':
            eliminar_dispositivo('\nIngrese el nombre del dispositivo que desee eliminar: ')
        elif opcion == '4':
            listar_dispositivos()
        elif opcion == '5':
            buscar_dispositivo()
        elif opcion == '0':
            menu_dispositivos = False
            return menu_dispositivos

# Menu Automatizaciones

def manipular_automatizaciones(msg, menu_automatizaciones):
    while True:
        opcion = input(msg).strip()
        if not introducir_opcion_3(opcion):
            continue
        elif opcion == '1':
            agregar_automatizacion()
        elif opcion == '2':
            modificar_automatizacion()
        elif opcion == '3':
            eliminar_automatizacion()
        elif opcion == '4':
            listar_automatizaciones()
        elif opcion == '0':
            menu_automatizaciones = False
            return menu_automatizaciones

# Menu Login

def menu_login(msg, login, exit):
    from sistema import usuarios_registro

    while True:
        codigo = input(msg).strip()

        match codigo:

            case '1':
                nombre = input("\nIngrese el nombre de usuario (minimo 3 caracteres): ")
                contraseña = input("\nIngrese la contraseña (minimo 8 caracteres, maximo 15 caracteres): ")

                if not validar_nombre_usuario(nombre):
                    print(f"\nEl nombre '{nombre}' no es valido, recuerde que debe ser mayor a 3 caracteres y solo puede utilizar los simbolos (. - _).")
                    continue

                if not validar_contraseña_usuario(contraseña):
                    print(f"\nLa contraseña no es valida, recuerde que debe ser entre 8-15 caracteres y solo puede utilizar los simbolos (. - _).")
                    continue

                eleccion = comparar_usuario(nombre, contraseña)
                if eleccion == "acceso":
                    print("Usuario logeado con exito.\n")
                    login = True
                    exit = False
                    return login, exit
                if eleccion == "contraseña_error":
                    print("Error: Contraseña incorrecta\n")
                    login = False
                    exit = False
                    return login, exit
                if eleccion == "usuario_error":
                    print("Error: Usuario no registrado\n")
                    login = False
                    exit = False
                    return login, exit
                
            case '2':
                nombre = input("Ingrese el nombre de usuario (minimo 3 caracteres): ")
                contraseña = input("Ingrese la contraseña (minimo 8 caracteres): ")
                if not validar_nombre_usuario(nombre):
                    print(f"El nombre {nombre} no es valido, recuerde que solo puede utilizar los simbolos (. - _)\n")
                    continue

                if not validar_contraseña_usuario(contraseña):
                    print(f"La contraseña no es valida, recuerde que solo puede utilizar los simbolos (. - _)\n")
                    continue

                for usuario in usuarios_registro:
                    if usuario.nombre == nombre:
                        print("Error: El usuario ya se encuentra registrado.\n")
                        login = False
                        exit = False
                        continue

                else:
                    registrar_usuario(nombre, contraseña)
                    print(f"Usuario {nombre} registrado, inicie sesion para utilizar el sistema")
                    login = False
                    exit = False
                    return login, exit
                        
            case '0':
                login = False
                exit = True
                return login, exit
                
            case _:
                print("Error: El codigo es erroneo, asegurese de no poner letras ni simbolos, solo numeros\n")