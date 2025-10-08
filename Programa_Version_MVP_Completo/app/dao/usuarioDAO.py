import bcrypt
from conn.conexion_base_de_datos import fetch_one, fetch_all, ejecutar_consulta
from dominio.usuario import Usuario

DEBUG_MODE = True

class UsuarioDAO:

    def obtener_por_nombre(nombre_usuario):
        fila = fetch_one('''
                        SELECT id_usuario, nombre_usuario, contrasena_usuario, id_rol_usuario
                        FROM Usuario 
                        WHERE nombre_usuario = ?''', (nombre_usuario,))
        if fila:
            return ({'id_usuario' : fila[0], 'nombre_usuario' : fila[1], 'contrasena_usuario' : fila[2], 'id_rol_usuario' : fila[3]}) if fila else None
    
    def obtener_id_usuario(id_usuario):
        fila = fetch_one('''
                        SELECT u.id_usuario, u.nombre_usuario, r.nombre_rol
                        FROM Usuario u
                        JOIN Rol r ON u.id_rol_usuario = r.id_rol
                        WHERE id_usuario = ?''', (id_usuario))
        return ({'id_usuario' : fila[0], 'nombre_usuario' : fila[1], 'nombre_rol' : fila[2]}) if fila else None

    def crear_usuario(usuario):
        ejecutar_consulta('''
                        INSERT INTO Usuario (nombre_usuario, contrasena_usuario, id_rol_usuario) 
                        VALUES (?, ?, ?)''',
                        (usuario[0], usuario[1], usuario[2]))
        
    def listar_usuarios():
        filas = fetch_all('''
                        SELECT u.id_usuario, u.nombre_usuario, u.contrasena_usuario, r.nombre_rol
                        FROM Usuario u
                        JOIN Rol r ON u.id_rol_usuario = r.id_rol''')
        return [Usuario(*fila) for fila in filas] if filas else None

    def imprimir_usuarios():
        fila = UsuarioDAO.listar_usuarios()
        print('-' * 70)
        print(f' {'ID':<5} {'Nombre':<25} {'Rol':<25}')
        print('-' * 70)
        for u in fila:
            print(f' {u.id_usuario:<5} {u.nombre_usuario:<25} {u.id_rol_usuario:<25}')
            print('-' * 70)

    def imprimir_usuario(nombre):
        fila = fetch_all('''
                        SELECT u.id_usuario, u.nombre_usuario, r.nombre_rol
                        FROM Usuario u
                        JOIN Rol r ON u.id_rol_usuario = r.id_rol
                        WHERE u.nombre_usuario = ?''', (nombre,))
        fila = fila[0]
        print('-' * 70)
        print(f' {'ID':<5} {'Nombre':<25} {'Rol':<25}')
        print('-' * 70)
        print(f' {fila[0]:<5} {fila[1]:<25} {fila[2]:<25}')
        print('-' * 70)

    def comparar_usuario(usuario):
        fila = UsuarioDAO.obtener_por_nombre(usuario[0])

        if fila is None:
            return 'usuario_error', None
        
        if DEBUG_MODE:
            acceso_correcto = usuario[1] == fila['contrasena_usuario']
        else:
            acceso_correcto = bcrypt.checkpw(usuario[1].encode('utf-8'), fila['contrasena_usuario'].encode('utf-8'))
        
        if acceso_correcto:
            usuario = (fila['nombre_usuario'], fila['contrasena_usuario'], fila['id_rol_usuario'])
            return 'acceso', usuario
        else:
            return 'contraseña_error', None

    def registrar_usuario(nombre, contraseña):
        fila = UsuarioDAO.obtener_por_nombre(nombre)
        if fila:
            print('Usuario ya registrado.\n')
            return False
        contraseña_hashed = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
        usuario = UsuarioDAO.listar_usuarios()
        rol = 1 if len(usuario) == 0 else 3
        UsuarioDAO.crear_usuario(usuario = (nombre, contraseña_hashed, rol))
        print(f'Usuario {nombre} registrado correctamente.\n')
        return True

    def actualizar_rol_usuario(rol, usuario):
        ejecutar_consulta('''
                        UPDATE Usuario 
                        SET id_rol_usuario = ?
                        WHERE id_usuario = ?''', (rol, usuario))
