# Dispositivos

class Tipos_Dispositivos:
    def __init__(self, nombre):
        self.nombre = nombre

class Dispositivos:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = obtener_estado('APAGADO')
        self.activo = False

class Estados:
    def __init__(self, nombre):
        self.nombre = nombre

tipos_dispositivos_registrados = []

dispositivos_registrados = []

estados_registrados = []

def obtener_tipo(nombre):
    for tipo in tipos_dispositivos_registrados:
        if tipo.nombre == nombre:
            return tipo

def obtener_estado(nombre):
    for estado in estados_registrados:
        if estado.nombre == nombre:
            return estado

def obtener_estado_indice(indice):
    if 0 <= indice < len(estados_registrados):
        return estados_registrados[indice]

tipos_dispositivos_preregistrados = [Tipos_Dispositivos(nombre = "luz"),
                                     Tipos_Dispositivos(nombre = "camara"),
                                     Tipos_Dispositivos(nombre = "puerta"),
                                     Tipos_Dispositivos(nombre = "ciclo"),
                                     Tipos_Dispositivos(nombre = "calefaccion")]

tipos_dispositivos_registrados.extend(tipos_dispositivos_preregistrados)

dispositivos_preregistrados = [Dispositivos("luz_del_living", obtener_tipo("luz")),
                               Dispositivos("camara_puerta", obtener_tipo("camara")),
                               Dispositivos("lavarropa", obtener_tipo("ciclo"))]

dispositivos_registrados.extend(dispositivos_preregistrados)

estados_preregistrados = [Estados(nombre = "ENCENDIDO"),
                          Estados(nombre = "APAGADO"),
                          Estados(nombre = "AHORRO_DE_ENERGIA"),
                          Estados(nombre = "MANTENIMIENTO")]

estados_registrados.extend(estados_preregistrados)

# Automatizaciones

class Automatizaciones:
    def __init__(self, nombre, dispositivo, hora_inicio, hora_fin, estado):
        self.nombre = nombre
        self.dispositivo = dispositivo
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin 
        self.estado = estado
        self.activado = False

automatizaciones_registradas = []

automatizaciones_preregistradas = [Automatizaciones(nombre = "centrifugar", dispositivo = dispositivos_registrados[2], hora_inicio = "06:19 PM", hora_fin = "08:15 AM", estado = obtener_estado("ENCENDIDO"))]

automatizaciones_registradas.extend(automatizaciones_preregistradas)

# Usuarios

class Roles:
    ADMIN = "administrador"
    USUARIO = "usuario"

class Usuarios:
    def __init__(self, nombre, contraseña, rol):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol

usuarios_registro = []