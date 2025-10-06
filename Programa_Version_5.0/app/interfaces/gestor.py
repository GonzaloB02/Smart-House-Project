from interfaces.validaciones import validar_nombre, validar_numero_entero, normalizar_nombre, validar_hora
from dao.dispositivoDAO import DispositivoDAO
from dao.tipo_dispositivoDAO import Tipo_DispositivoDAO
from dao.estadoDAO import EstadoDAO
from dao.automatizacionDAO import AutomatizacionDAO
from dao.usuarioDAO import UsuarioDAO
from dao.rolDAO import RolDAO

# Agregar dispositivos

def agregar_dispositivo():
    while True:

        DispositivoDAO.imprimir_dispositivos_activos()
        nombre = normalizar_nombre(validar_nombre("Nombre del dispositivo: "))

        if DispositivoDAO.buscar_existencia_nombre(nombre):
            DispositivoDAO.re_activar(nombre) if DispositivoDAO.dispositivo_activo(nombre) == None else print(f'El dispositivo {nombre} ya se encuentra registrado') 
            print(f"Dispositivo {nombre} agregado correctamente.\n")
            return

        Tipo_DispositivoDAO.imprimir_tipos_dispositivos()
        tipo_dispositivo_eleccion = validar_numero_entero("Seleccione un tipo de dispositivo (numerico): ")

        if not Tipo_DispositivoDAO.obtener_id_tipo_dispositivo(tipo_dispositivo_eleccion):
            print("Seleccion erronea, el tipo debe estar dentro del rango\n")
            continue

        DispositivoDAO.crear_dispositivo(nombre, tipo_dispositivo_eleccion, id_estado=2, activo=1)
        print(f"Dispositivo {nombre} agregado correctamente.\n")
        return 
    
# Modificar Dispositivo

def modificar_dispositivo():
    while True:

        DispositivoDAO.imprimir_dispositivos_activos()
        id_dispositivo = validar_numero_entero('\nIngrese el ID del dispositivo que desea modificar: ')
        
        if DispositivoDAO.obtener_id_dispositivo(id_dispositivo) is None:
            print('El dispositivo que intenta seleccionar esta fuera de rango.\n')
            continue

        nuevo_nombre_dispositivo = normalizar_nombre(validar_nombre('\nIngrese el nuevo nombre del dispositivo: '))

        if DispositivoDAO.buscar_existencia_nombre(nuevo_nombre_dispositivo):
            print('El nombre que intenta utilizar ya esta registrado.\n')
            continue

        Tipo_DispositivoDAO.imprimir_tipos_dispositivos()
        id_tipo_dispositivo = validar_numero_entero('\nIngrese el nuevo tipo de dispositivo (NUMERICO): ')
        
        if Tipo_DispositivoDAO.obtener_id_tipo_dispositivo(id_tipo_dispositivo) is None:
            print('El tipo que intenta seleccionar se encuentra fuera de rango.\n')
            continue

        EstadoDAO.imprimir_estados()
        id_estado = validar_numero_entero('\nSeleccione el nuevo estado: ')

        if EstadoDAO.obtener_id_estado(id_estado) is None:
            print('El estado que intenta seleccionar se encuentra fuera de rango.\n')
            continue

        DispositivoDAO.actualizar_dispositivo(dispositivo = (nuevo_nombre_dispositivo, id_tipo_dispositivo, id_estado, id_dispositivo))
        print(f"\nDispositivo {nuevo_nombre_dispositivo} modificado correctamente.\n")
        return

# Eliminar dispositivos

def eliminar_dispositivo():

    DispositivoDAO.imprimir_dispositivos_activos()
    id_eleccion = validar_numero_entero('\nIngrese el numero del dispositivo que desee eliminar: ')

    if not DispositivoDAO.obtener_id_dispositivo(id_eleccion):
        print('Dispositivo no encontrado. \n')
        return
    
    confirmacion = validar_numero_entero('Ingrese el ID de nuevo para confirmar: ')

    if confirmacion == id_eleccion:
        DispositivoDAO.eliminar_dispositivo(id_eleccion)
        print('Dispositivo eliminado.\n')
    else:
        print('Eliminación cancelada.\n')

# Listar dispositivos

def listar_dispositivos():
    DispositivoDAO.imprimir_dispositivos_activos()

# Buscar dispositivos

def buscar_dispositivo():
    nombre = normalizar_nombre(input('\nIngrese el nombre del dispositivo que desea buscar: ')).strip()
    
    if DispositivoDAO.buscar_existencia_nombre(nombre):
        DispositivoDAO.imprimir_busqueda(nombre)
        return
    else:
        print('Dispositivo no encontrado.\n')

# Agregar automatizaciones

def agregar_automatizacion():
    while True:

        AutomatizacionDAO.imprimir_automatizaciones()
        nombre = normalizar_nombre(validar_nombre("Introduzca el nombre de la automatizacion: "))
        
        if AutomatizacionDAO.buscar_existencia_nombre(nombre):
            AutomatizacionDAO.re_activar_automatizacion(nombre) if AutomatizacionDAO.automatizacion_activa(nombre)[0] == False else print(f"La automatización {nombre} ya existe.\n")
            print("Automatizacion agregada con exito")
            return

        DispositivoDAO.imprimir_dispositivos()
        dispositivo_indice = validar_numero_entero("Seleccione un dispositivo: ")
        
        if DispositivoDAO.obtener_id_dispositivo(dispositivo_indice) is None:
            print("Error: Ingrese uno de los numeros listados que sean validos\n")
            continue

        EstadoDAO.imprimir_estados()
        estado_eleccion = validar_numero_entero("Seleccione un estado: ")

        if EstadoDAO.obtener_id_estado(estado_eleccion) is None:
            print("Error: Ingrese uno de los numeros listados que sean validos\n")
            continue

        hora_inicio = validar_hora("Ingrese el horario el cual debe de iniciar la accion (Use el horario militar, es decir, 8:30PM => 2030): ")
        hora_fin = validar_hora("Ingresar el horario el cual debe de finalizar la accion (Use el horario militar, es decir, 8:30PM => 2030):")
        
        if hora_inicio == hora_fin:
            print('\nError: La hora de inicio y final no pueden ser iguales, elija una hora final distinta a la hora de inicio.')
            continue

        AutomatizacionDAO.crear_automatizacion(nombre, dispositivo_indice, estado_eleccion, hora_inicio, hora_fin)
        print("Automatizacion agregada con exito")
        return

# Modificar automatizaciones

def modificar_automatizacion():
    while True:

        AutomatizacionDAO.imprimir_automatizaciones()
        auto_eleccion = validar_numero_entero("Ingrese el ID de la automatizacion que desea modificar: ")

        if AutomatizacionDAO.obtener_id_automatizacion(auto_eleccion) is None:    
            print(f"La automatizacion seleccinada esta fuera de rango no fue hallada.\n")
            continue

        nueva_hora_inicio = validar_hora("Ingrese el horario que desea que inicie la automatizacion: ")
        nueva_hora_fin = validar_hora("Ingrese el horario que desea que finalice la automatizacion: ")

        if nueva_hora_inicio == nueva_hora_fin:
            print('\nError: La hora de inicio y final no pueden ser iguales, elija una hora final distinta a la hora de inicio.')
            continue

        EstadoDAO.imprimir_estados()
        nuevo_estado = validar_numero_entero("Seleccione el estado que desea que cambie automaticamente: ")

        if EstadoDAO.obtener_id_estado(nuevo_estado) is None:
            print("Error: Ingrese uno de los numeros listados que sean validos\n")
            continue 

        AutomatizacionDAO.actualizar_automatizacion(auto_eleccion, nuevo_estado, nueva_hora_inicio, nueva_hora_fin)
        print('La automatizacion fue actualizada exitosamente\n')
        return


# Eliminar automatizaciones

def eliminar_automatizacion():
    while True:
        AutomatizacionDAO.imprimir_automatizaciones()
        id_automatizacion = validar_numero_entero("Ingrese el ID de la automatizacion a eliminar: ")
       
        if AutomatizacionDAO.obtener_id_automatizacion(id_automatizacion) is None:
            print(f'La automatizacion {id_automatizacion} no fue hallada.\n')
            continue

        confirmacion = validar_numero_entero('Ingrese el ID de nuevo para confirmar: ')

        if confirmacion == id_automatizacion:
            AutomatizacionDAO.eliminar_automatizacion(id_automatizacion)
            print('La automatizacion fue eliminada exitosamente.\n')
        else:
            print('Eliminacion cancelada.\n')
        return

# Listar Automatizaciones

def listar_automatizaciones():
    AutomatizacionDAO.imprimir_automatizaciones()

# Modificar Rol Usuario

def modificar_rol_usuario():
    while True:
        
        UsuarioDAO.imprimir_usuarios()
        usuario_eleccion = validar_numero_entero('Ingrese el ID del usuario que desea modificar: ')

        if UsuarioDAO.obtener_id_usuario(usuario_eleccion) is None:
            print('El usuario que desea seleccionar se encuentra fuera de rango.\n')
            continue
        
        RolDAO.imprimir_roles()
        rol_eleccion = validar_numero_entero('Ingrese el ID del rol que desea designarle al usuario: ')

        if RolDAO.obtener_id_rol(usuario_eleccion) is None:
            print('El rol que desea seleccionar se encuentra fuera de rango.\n')
            continue

        UsuarioDAO.actualizar_rol_usuario(rol_eleccion, usuario_eleccion)
        print('El rol del usuario se actualizo con exito.\n')
        return

def buscar_usuario():
        nombre = normalizar_nombre(input('Ingrese el nombre del usuario que desea buscar: '))
        UsuarioDAO.imprimir_usuario(nombre) if UsuarioDAO.obtener_por_nombre(nombre) is not None else print('Usuario no encontrado.\n')

def listar_usuarios():
    UsuarioDAO.imprimir_usuarios()
    
