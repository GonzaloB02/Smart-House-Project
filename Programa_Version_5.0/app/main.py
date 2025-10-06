#from eventos import simular_sensor, simular_camara_puerta
#import threading
#from monitoreo import monitorizacion_automatica

from interfaces.interfaz import menu_login, menu_intermedio, manipular_roles, manipular_automatizaciones, manipular_dispositivos

def main():
        
        login = False
        exit = False
        menu_dispositivos = False
        menu_automatizaciones = False
        menu_rol = False
        monitorizacion_activa = False
        usuario = ()

        # Simular eventos

        #simular_sensor()
        #simular_camara_puerta()

        while not exit: 
            if not login:
                login, exit, usuario = menu_login('''
                Ingrese una de las siguientes opciones
                1. Loguear usuario.
                2. Registrar usuario.
                0. Salir.
                -''', login, exit, usuario)
            
            elif not menu_dispositivos and not menu_automatizaciones and not menu_rol:
                login, menu_dispositivos, menu_automatizaciones, menu_rol = menu_intermedio('''
                Ingrese una de las siguientes opciones
                1. Administrar dispositivos.
                2. Administrar automatizaciones.
                9. Modificar rol a un usuario.
                0. Volver al menu de log-in.
                -''', login, menu_dispositivos, menu_automatizaciones, menu_rol)

            elif menu_dispositivos:
                usuario, menu_dispositivos = manipular_dispositivos('''
                Ingrese una de las siguientes opciones
                1. Agregar dispositivo.
                2. Modificar dispositivo.
                3. Eliminar dispositivo.
                4. Listar dispositivos.
                5. Buscar dispositivo.
                0. Volver al menu principal.
                -''', usuario, menu_dispositivos)

            elif menu_automatizaciones:
                usuario, menu_automatizaciones = manipular_automatizaciones('''
                Ingrese una de las siguientes opciones
                1. Agregar automatizacion.
                2. Modificar automatizacion.
                3. Eliminar automatizacion.
                4. Listar automatizaciones.
                0. Volver al menu principal.
                -''', usuario, menu_automatizaciones)

            elif menu_rol:
                 usuario, menu_rol = manipular_roles('''
                Ingrese una de las siguientes opciones
                1. Modificar rol a usuario.
                2. Buscar usuario.
                3. Listar usuarios.
                0. Volver al menu principal.
                -''', usuario, menu_rol)

            # if login and not monitorizacion_activa:
            #     threading.Thread(target=monitorizacion_automatica, daemon=True).start()
            #     monitorizacion_activa = True

if __name__ == "__main__":
    main()