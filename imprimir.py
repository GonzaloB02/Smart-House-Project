from sistema import dispositivos_registrados, estados_registrados, tipos_dispositivos_registrados, automatizaciones_registradas

def imprimir_dispositivos():
    print("-" * 20)
    print(f" {'Dispositivos registrados':<25}")
    print("-" * 20)
    #print("0. Añadir nuevo dispositivo.")

    for i, dispositivo in enumerate(dispositivos_registrados):
        print(f"{i + 1}. {dispositivo.nombre}.")
        print("-" * 20)
    print("\n")

def imprimir_estados():
    print("-" * 20)
    print(f" {'Estados':<25}")
    print("-" * 20)
    #print("0. Agregar nuevo estado.")

    for i, estado in enumerate(estados_registrados):
        print(f"{i + 1}. {estado.nombre}.")
        print("-" * 20)
    print("\n")

def imprimir_tipos_dispositivos():
    print("-" * 20)
    print(f" {'Tipo':<25}")
    print("-" * 20)
    print("0. Añadir nuevo tipo dispositivo.")

    for i, tipo in enumerate(tipos_dispositivos_registrados):
        print(f"{i + 1}. {tipo.nombre}")
        print("-" * 20)
    print("\n")

def imprimir_automatizaciones():
    print("-" * 130)
    print(f" {'Nombre':<25} {'Dispositivos':<25} {'Hora Inicio':<25} {'hora_fin':<25} {'Estado'}")
    print("-" * 130)

    for i, auto in enumerate(automatizaciones_registradas):
        nombre = auto.nombre
        dispositivo = auto.dispositivo.nombre
        hora_inicio = auto.hora_inicio
        hora_fin = auto.hora_fin
        estado = auto.estado.nombre
        print(f"{nombre:<25} {dispositivo:<25} {hora_inicio:<25} {hora_fin:<25}  {estado}")
        print("-" * 130)
    print("\n")
