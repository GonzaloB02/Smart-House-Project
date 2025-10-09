USE SmartHouse;
GO

SELECT * FROM Tipo_Dispositivo;
SELECT * FROM Estado;
SELECT * FROM Dispositivo;
SELECT * FROM Automatizacion;
SELECT * FROM Usuario;
SELECT * FROM Rol;

-- Consultar todos los datos en cada tabla

INSERT INTO Rol (nombre_rol) VALUES ('ADMIN');
INSERT INTO Rol (nombre_rol) VALUES ('USUARIO');
INSERT INTO Rol (nombre_rol) VALUES ('INVITADO');

-- Inserta nombre de roles en la tabla rol

INSERT INTO Usuario (nombre_usuario, contrasena_usuario, id_rol_usuario) VALUES ('admin', 'hash_admin', 1)
INSERT INTO Usuario (nombre_usuario, contrasena_usuario, id_rol_usuario) VALUES ('usuario1', 'hash_usuario1', 2)
INSERT INTO Usuario (nombre_usuario, contrasena_usuario, id_rol_usuario) VALUES ('usuario2', 'hash_usuario2', 2)
INSERT INTO Usuario (nombre_usuario, contrasena_usuario, id_rol_usuario) VALUES ('invitado', 'hash_invitado', 3)

-- Inserta el nombre, contraseña y el rol de los usuarios

INSERT INTO Estado (nombre_estado) VALUES ('ENCENDIDO');
INSERT INTO Estado (nombre_estado) VALUES ('APAGADO');
INSERT INTO Estado (nombre_estado) VALUES ('AHORRO DE ENERGIA');
INSERT INTO Estado (nombre_estado) VALUES ('MANTENIMIENTO');

-- Inserta el nombre de los estados

INSERT INTO Tipo_Dispositivo (nombre_tipo_dispositivo) VALUES ('luz');
INSERT INTO Tipo_Dispositivo (nombre_tipo_dispositivo) VALUES ('camara');
INSERT INTO Tipo_Dispositivo (nombre_tipo_dispositivo) VALUES ('sensor');

-- Inserta el nombre de los tipos de dispositivos

INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('luz_cocina', 1 ,2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('luz_patio', 1, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('luz_living', 1, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('luz_frente', 1, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('camara_patio', 2, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('camara_living', 2, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('camara_frente', 2, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('sensor_living', 3, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('sensor_patio', 3, 2, 1);
INSERT INTO Dispositivo (nombre_dispositivo, id_tipo_dispositivo, id_estado, activo) VALUES ('sensor_frente', 3, 2, 1);

-- Inserta el nombre, tipo, estado y estado de activacion de los dispositivos

INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('prender_luz_cocina', 1,'19:00:00', '00:00:00', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('prender_luz_patio', 2, '18:30:00', '07:00:00', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('prender_luz_living', 3, '18:45:00', '00:30:00', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado ,activo) VALUES ('prender_luz_frente', 4, '18:50:00', '07:30:00', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('camara_foto_informe_patio', 5, '00:00:00', '23:59:59', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('camara_foto_informe_living', 6, '00:00:00', '23:59:59', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('camara_foto_informe_frente', 7, '00:00:00', '23:59:59', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('sensor_activacion_living', 8, '00:00:00', '23:59:59', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('sensor_activacion_patio', 9, '00:00:00', '23:59:59', 1, 1);
INSERT INTO Automatizacion (nombre_automatizacion, id_dispositivo, hora_inicio, hora_fin, id_estado, activo) VALUES ('sensor_activacion_frente', 10, '00:00:00', '23:59:59', 1, 1);

-- Inserta el nombre, dispositivo, estado, hora inicio, hora fin, y estado de activacion de las automatizaciones

SELECT u.id_usuario, u.nombre_usuario, r.nombre_rol 
FROM Usuario u 
JOIN Rol r ON u.id_rol_usuario = r.id_rol;

-- Selecciona todos los usuarios registrados uniendo el nombre de su rol y muestra sus atributos

SELECT a.id_automatizacion, a.nombre_automatizacion, d.nombre_dispositivo, e.nombre_estado, a.hora_inicio, a.hora_fin
FROM Automatizacion a 
JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
JOIN Estado e ON a.id_estado = e.id_estado
WHERE a.activo = 1;

-- Selecciona todas las automatizaciones registradas y activas uniendo el nombre del dispositivo asociado, su estado y muestra todos sus atributos 

SELECT d.id_dispositivo, d.nombre_dispositivo, t.nombre_tipo_dispositivo, e.nombre_estado
FROM Dispositivo d
JOIN Tipo_Dispositivo t ON d.id_tipo_dispositivo = t.id_tipo_dispositivo
JOIN Estado e ON d.id_estado = e.id_estado;

-- Selecciona todos los dispositivos registrados uniendo el nombre de su tipo, estado y muestra sus atributos

SELECT d.nombre_dispositivo, a.nombre_automatizacion
FROM Dispositivo d  
INNER JOIN Automatizacion a ON d.id_dispositivo = a.id_dispositivo;

-- Selecciona todos los dispositivos que estan vinculados a una automatizacion y muestra sus nombres

SELECT nombre_dispositivo
FROM Dispositivo 
WHERE id_dispositivo = (
	SELECT TOP 1 id_dispositivo
	FROM Automatizacion 
	GROUP BY id_dispositivo
	ORDER BY COUNT(*) DESC
);

-- Selecciona el dispositivo que este vinculado a la mayor cantidad de automatizaciones

SELECT u.nombre_usuario, r.nombre_rol
FROM Usuario u
JOIN Rol r ON u.id_rol_usuario = r.id_rol
WHERE r.id_rol IN (
	SELECT TOP 2 id_rol
	FROM Rol
	GROUP BY id_rol
	ORDER BY id_rol ASC
);

-- Selecciona a los usuarios cuyos roles sean mayor a 'USUARIO'
