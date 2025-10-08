def validar_nombre(msg):
    while True:
        valor = input(msg).lower().strip()
        if all(char.replace('_', '').isalpha() or char.isspace() for char in valor) and len(valor) > 1:
            return valor
        print("\nNombre no valido, recuerde que los simbolos no son validos.")
        eleccion = input("\n¿Desea cancelar la accion? (SI/NO): ").lower()
        if eleccion == 'si':
            return None
        if eleccion == 'no':
            continue
        else:
            print("Error: Eleccion no identificada, recuerde que debe poner 'SI' o 'NO': ")

def validar_numero_entero(msg):
    while True:
        numero = input(msg)
        if numero.isdigit() and int(numero) > 0 and len(numero) > 0:
            return int(numero)
        print("Ingrese un numero valido, no debe contener decimales ni simbolos\n")
        eleccion = input("\n¿Desea cancelar la accion? (SI/NO): ").lower()
        if eleccion == 'si':
            return None
        if eleccion == 'no':
            continue
        else:
            print("Error: Eleccion no identificada, recuerde que debe poner 'SI' o 'NO': ")

def validar_numero_flotante(msg):
    while True:
        numero = input(msg)
        if numero.count(".") <= 1 and numero.replace('.', '').isdigit() <= 1 and int(numero) > 0 and len(numero) > 0:
            return float(numero)
        print("Ingrese un numero valido, no debe contener simbolos\n")
        eleccion = input("\n¿Desea cancelar la accion? (SI/NO): ").lower()
        if eleccion == 'si':
            return None
        if eleccion == 'no':
            continue
        else:
            print("Error: Eleccion no identificada, recuerde que debe poner 'SI' o 'NO': ")

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
            eleccion = input("\n¿Desea cancelar la accion? (SI/NO): ").lower()
            if eleccion == 'si':
                return None
            if eleccion == 'no':
                continue
            else:
                print("Error: Eleccion no identificada, recuerde que debe poner 'SI' o 'NO': ")

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
    if nombre is None:
        return None
    return nombre.replace(' ', '_')



