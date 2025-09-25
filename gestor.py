from validaciones import validar_nombre, validar_numero_entero, normalizar_nombre, validar_hora
from sistema import Dispositivos, Automatizaciones, dispositivos_registrados, tipos_dispositivos_registrados, automatizaciones_registradas, estados_registrados, obtener_estado_indice
from imprimir import imprimir_tipos_dispositivos, imprimir_dispositivos, imprimir_estados, imprimir_automatizaciones

# Agregar dispositivos

def agregar_dispositivo():
    while True:
        imprimir_tipos_dispositivos()
        nombre = normalizar_nombre(validar_nombre("Nombre del dispositivo: "))
        tipo = validar_numero_entero("Seleccione un tipo de dispositivo (numerico): ")
        #if tipo == '0':
            #tipo_final = validar_nombre("Ingrese en nombre del tipo de dispostivo: ")
            #Completar luego
        if tipo < 1 or tipo > len(tipos_dispositivos_registrados):
            print("Seleccion erronea, el tipo debe estar dentro del rango\n")
            continue
        tipo_final = tipos_dispositivos_registrados[tipo - 1]

        if any(u.nombre == nombre for u in dispositivos_registrados):
                print(f"El dispositivo {nombre} ya se encuentra registrado.\n")
                return        
        nuevo_dispositivo = Dispositivos(nombre, tipo_final)
        dispositivos_registrados.append(nuevo_dispositivo)
        print(f"Dispositivo {nombre} agregado correctamente.\n")
        return

# Modificar Dispositivo

def modificar_dispositivo():
    while True:
        imprimir_dispositivos()
        nombre = normalizar_nombre(validar_nombre('\nIngrese el nombre del dispositivo: '))
        for dispositivo in dispositivos_registrados:
            if dispositivo.nombre == nombre:
                print("-" * 70)
                print(f" {'Nombre':<25} {'Tipo':<25}")
                print("-" * 70)            
                print(f"{dispositivo.nombre:<25} {dispositivo.tipo.nombre:<25}")
                print("-" * 70)
        nuevo_nombre = normalizar_nombre(validar_nombre('\nIngrese el nuevo nombre del dispositivo: '))
        imprimir_tipos_dispositivos()
        tipo = validar_numero_entero("\nSeleccione un tipo de dispositivo (numerico): ")
        if tipo < 1 or tipo > len(tipos_dispositivos_registrados):
            print("\nSeleccion erronea, el tipo debe estar dentro del rango\n")
            continue
        tipo_final = tipos_dispositivos_registrados[tipo - 1]

        if any(u.nombre == nombre for u in dispositivos_registrados):
                print(f"\nEl dispositivo {nombre} ya se encuentra registrado.\n")
                return        
        for dispositivo in dispositivos_registrados:
            if dispositivo.nombre == nombre:
                dispositivo.nombre = nuevo_nombre
                dispositivo.tipo = tipo_final
        print(f"\nDispositivo {nuevo_nombre} modificado correctamente.\n")
        return

# Eliminar dispositivos

def eliminar_dispositivo(msg):
    nombre = normalizar_nombre(input(msg))

    for dispositivo in (dispositivos_registrados):
        if dispositivo.nombre == nombre:
            dispositivos_registrados.remove(dispositivo)
            print(f"El dispositivo {nombre} fue eliminado exitosamente\n")
            return
    print(f"El dispositivo {nombre} no fue hallado\n")

# Listar dispositivos

def listar_dispositivos():
    imprimir_dispositivos()

# Buscar dispositivos

def buscar_dispositivo(msg):
    nombre = input(msg).strip()
    nombre = normalizar_nombre(nombre)

    for dispositivo in dispositivos_registrados:
        if dispositivo.nombre == nombre:
            print("-" * 70)
            print(f" {'Nombre':<25} {'Tipo':<25}")
            print("-" * 70)            
            print(f"{dispositivo.nombre:<25} {dispositivo.tipo.nombre:<25}")
            print("-" * 70)
            return
        
    print(f"El dispositivo {nombre} no fue hallado\n")

# Agregar automatizaciones

def agregar_automatizacion():

    nombre = normalizar_nombre(validar_nombre("Introduzca el nombre de la automatizacion: "))

    if any(a.nombre == nombre for a in automatizaciones_registradas):
        print(f"La automatización {nombre} ya existe.\n")
        return
    imprimir_dispositivos()

    dispositivo_indice = validar_numero_entero("Seleccione un dispositivo: ")
    if not (1 <= dispositivo_indice <= len(dispositivos_registrados)):
        print("Error: Ingrese uno de los numeros listados que sean validos\n")
        return
    dispositivo = dispositivos_registrados[dispositivo_indice - 1]
    imprimir_estados()

    estado_indice = validar_numero_entero("Seleccione un estado: ")
    if not (1 <= estado_indice <= len(estados_registrados)):
        print("Error: Ingrese uno de los numeros listados que sean validos\n")
        return
    estado_final = obtener_estado_indice(estado_indice - 1)
    
    hora_inicio = validar_hora("Ingrese el horario el cual debe de iniciar la accion (Use el horario militar, es decir, 8:30PM => 2030): ")
    hora_fin = validar_hora("Ingresar el horario el cual debe de finalizar la accion (Use el horario militar, es decir, 8:30PM => 2030):")
    if hora_inicio == hora_fin:
        print('\nError: La hora de inicio y final no pueden ser iguales, elija una hora final distinta a la hora de inicio.')
        return

    nueva_automatizacion = Automatizaciones(nombre, dispositivo, hora_inicio, hora_fin, estado_final)
    automatizaciones_registradas.append(nueva_automatizacion)
    print("Automatizacion agregada con exito")

# Modificar automatizaciones

def modificar_automatizacion():
    imprimir_automatizaciones()

    nombre = normalizar_nombre(validar_nombre("Ingrese el nombre de la automatizacion que desea modificar: "))
    auto = next((auto for auto in automatizaciones_registradas if auto.nombre == nombre), None)
    if not auto:    
        print(f"La automatizacion {nombre} no fue hallada.\n")
        return
    
    print("-" * 130)
    print(f" {'Nombre':<25} {'Dispositivos':<25} {'Hora Inicio':<25} {'Hora Fin':<25} {'Estado'}")
    print("-" * 130)
    dispositivo = auto.dispositivo.nombre
    hora_inicio = auto.hora_inicio
    hora_fin = auto.hora_fin
    estado = auto.estado.nombre
    print(f"{nombre:<25} {dispositivo:<25} {hora_inicio:<25} {hora_fin:<25} {estado}")
    print("-" * 130)

    nueva_hora_inicio = validar_hora("Ingrese el horario que desea que inicie la automatizacion: ")
    nueva_hora_fin = validar_hora("Ingrese el horario que desea que finalice la automatizacion: ")
    if nueva_hora_inicio == nueva_hora_fin:
        print('\nError: La hora de inicio y final no pueden ser iguales, elija una hora final distinta a la hora de inicio.')
        return
    imprimir_estados()

    cambiar_estado = validar_numero_entero("Seleccione el estado que desea que cambie automaticamente: ")
    if not (1 <= cambiar_estado <= len(estados_registrados)):
        print("Error: Ingrese uno de los numeros listados que sean validos\n")
        return
    cambiar_estado = obtener_estado_indice(cambiar_estado - 1) 
    
    auto.hora_inicio = nueva_hora_inicio
    auto.hora_fin = nueva_hora_fin
    auto.estado = cambiar_estado
    print(f"La automatizacion {nombre} fue actualizada exitosamente\n")

# Eliminar automatizaciones

def eliminar_automatizacion():
    imprimir_automatizaciones()
    
    nombre = normalizar_nombre(validar_nombre("Ingrese el nombre de la automatizacion a eliminar: "))

    for automatizacion in automatizaciones_registradas:
        if automatizacion.nombre == nombre:
            automatizaciones_registradas.remove(automatizacion)
            print(f"La automatizacion {nombre} fue eliminado exitosamente\n")
            return
    print(f"La automatizacion {nombre} no fue hallado")

# Listar Automatizaciones

def listar_automatizaciones():
    imprimir_automatizaciones()