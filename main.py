from conexion_base_de_datos import obtener_conexion, pyodbc
from eventos import simular_sensor, simular_camara_puerta
import threading
from monitoreo import monitorizacion_automatica
from interfaz import menu_login, menu_intermedio, manipular_dispositivos, manipular_automatizaciones

def main():

    try:
        conn = obtener_conexion()
        print('Conexion establecida.\n')

        login = False
        exit = False
        menu_dispositivos = False
        menu_automatizaciones = False
        monitorizacion_activa = False

        # Simular eventos

        #simular_sensor()
        #simular_camara_puerta()

        while not exit: 
            if not login:
                login, exit = menu_login('''
                1. Loguear usuario.
                2. Registrar usuario.
                0. Salir.
                -''', login, exit)
            
            elif not menu_dispositivos and not menu_automatizaciones:
                login, menu_dispositivos, menu_automatizaciones = menu_intermedio('''
                1. Administrar dispositivos.
                2. Administrar automatizaciones.
                0. Volver al menu de log-in.
                -''', login, menu_dispositivos, menu_automatizaciones)

            elif menu_dispositivos:
                menu_dispositivos = manipular_dispositivos('''
                1. Agregar dispositivo.
                2. Modificar dispositivo.
                3. Eliminar dispositivo.
                4. Listar dispositivos.
                5. Buscar dispositivo.
                0. Volver al menu principal.
                -''', menu_dispositivos)

            elif menu_automatizaciones:
                menu_automatizaciones = manipular_automatizaciones('''
                1. Agregar automatizacion.
                2. Modificar automatizacion.
                3. Eliminar automatizacion.
                4. Listar automatizaciones.
                0. Volver al menu principal.
                -''', menu_automatizaciones)

            if login and not monitorizacion_activa:
                threading.Thread(target=monitorizacion_automatica, daemon=True).start()
                monitorizacion_activa = True

    except Exception as e:
        print("Error de conexión:", e)

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()