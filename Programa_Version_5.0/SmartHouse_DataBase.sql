CREATE TABLE Rol(
	id_rol INT PRIMARY KEY IDENTITY(1,1),
	nombre_rol VARCHAR (15) NOT NULL
);

CREATE TABLE Usuario(
	id_usuario INT PRIMARY KEY IDENTITY(1,1),
	nombre_usuario VARCHAR(20) NOT NULL,
	contrasena_usuario VARCHAR(75) NOT NULL,
	id_rol_usuario INT NOT NULL,
	FOREIGN KEY (id_rol_usuario) REFERENCES Rol (id_rol)
);

CREATE TABLE Tipo_Dispositivo(
	id_tipo_dispositivo INT PRIMARY KEY IDENTITY(1,1),
	nombre_tipo_dispositivo VARCHAR(50) NOT NULL
);

CREATE TABLE Estado(
	id_estado INT PRIMARY KEY IDENTITY(1,1),
	nombre_estado VARCHAR(50) NOT NULL
);

CREATE TABLE Dispositivo(
	id_dispositivo INT PRIMARY KEY IDENTITY(1, 1),
	id_estado INT NOT NULL,
	id_tipo_dispositivo INT NOT NULL,
	nombre_dispositivo VARCHAR(70),
	activo BIT NOT NULL,
	FOREIGN KEY (id_estado) REFERENCES Estado (id_estado),
	FOREIGN KEY (id_tipo_dispositivo) REFERENCES Tipo_Dispositivo (id_tipo_dispositivo)
);

CREATE TABLE Automatizacion(
	id_automatizacion INT PRIMARY KEY IDENTITY(1,1),
	id_dispositivo INT NOT NULL,
	id_estado INT NOT NULL,
	nombre_automatizacion VARCHAR(50) NOT NULL,
	hora_inicio DATETIME NOT NULL,
	hora_fin DATETIME NOT NULL,
	activo BIT NOT NULL,
	FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo (id_dispositivo),
	FOREIGN KEY (id_estado) REFERENCES Estado (id_estado)
);

USE SmartHouse;
GO
SELECT * FROM Tipo_Dispositivo;
SELECT * FROM Estado;
SELECT * FROM Dispositivo;
SELECT * FROM Automatizacion;
SELECT * FROM Usuario;
SELECT * FROM Rol;


 