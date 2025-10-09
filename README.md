SmartHouse ABP

Descripción del proyecto:
SmartHouse es un sistema de automatización de dispositivos domésticos desarrollado en Python + SQL Server Management, diseñado para optimizar recursos, mejorar la eficiencia energética y facilitar la gestión del hogar.

El sistema permite a los usuarios:
-	Registrar y autenticar usuarios con roles diferenciados (ADMIN, USUARIO, INVITADO).
-	Gestionar dispositivos y automatizaciones mediante operaciones CRUD.
-	Controlar accesos, estados y automatizaciones programadas de manera segura.
Este proyecto corresponde a la Actividad Integradora ABP – Programación I – Base de Datos – Ética y Deontología de la Tecnicatura de Desarrollo de Software.

Estado Actual
Versión: MVP Funcional (consola).
Estado: Finalizado y estable.
Tecnologías Principales:
-	Python 3.10+
-	SQL Server Management 2020.
-	PyODBC.
-	Bcrypt.

 Instalación y Configuración:
1.	Clonar el repositorio de GitHub.
2.	Instalar dependencias (PyODBC, Bcrypt).
3.	Configurar la Base de Datos: 
-	 Abrir SQL Server 
-	Ejecutar los scripts:
DDL_SmartHouse.sql
DML_SmartHouse.sql
-	Asegurarse de crear la base de datos SmartHouse antes de ejecutar los inserts.
4.	Configurar conexión:
Editar el archivo “conexion_base_de_datos.py” con las credenciales locales del servidor SQL.
5.	Ejecutar el sistema desde main.py

Roles de Usuario
ADMIN
Permisos: Gestionar usuarios, roles, dispositivos y automatizaciones.
USUARIO
Permisos: Consultar, agregar y modificar dispositivos o automatizaciones.
INVITADO
Permisos: Solo consultar.

Funcionalidades Principales
-	Registro e inicio de sesión con contraseñas hasheadas (bcrypt).
-	Control de acceso por roles.
-	CRUD completo para dispositivos y automatizaciones.
-	Consultas SQL integradas (JOIN, subconsultas, relaciones).
-	Validaciones de datos y manejo de errores de entrada.
-	Baja lógica (activo = 0) para mantener integridad de datos.

Estructura del Proyecto
dominio: Clases del modelo (Usuario, Rol, Dispositivo, Automatizacion).
dao: Clases DAO (acceso a datos).
conn: Conexión a base de datos SQL (PyODBC).
interfaces: Menús y navegación principal del usuario.
base_de_datos: Scripts DML y DDL de la estructura e inserciones a la base de datos SQL.
documentacion.pdf: Diagramas DER, Relacional y de Clases.
main.py: Punto de ejecución del programa.
Informe_Impacto_Tecnologico.pdf: Informe detallado sobre el funcionamiento e impacto del programa en distintas áreas. 

Pilares AWS-Well Architected Aplicados
1.	Operational Excellence: Modularidad en capas, separación DAO, mantenimiento simple.
2.	Security: Contraseñas cifradas, control de roles y validaciones de entrada.
3.	Reliability: Claves foráneas, bajas lógicas y estructura estable ante fallos.
4.	Performance Efficiency: Consultas SQL optimizadas y código escalable.
5.	Cost Optimization: Ejecución local, modularidad, automatización del consumo energético.
6.	Sustainability: Automatizaciones programadas orientadas al ahorro y la eficiencia.

Documentación y Recursos
Informe_Impacto_Tecnologico.pdf: Análisis ético, social y ambiental del sistema.
docs: Diagramas de clases, DER y modelo relacional.
ReadMe_Base_de_Datos.pdf: Instrucción de ejecución SQL.

Roadmap Futuro
-	Integración de interfaz gráfica (GUI).
-	Implementación de TDD y pruebas unitarias.
-	Monitoreo en tiempo real de dispositivos IoT.
-	Reportes y análisis (KPI’s).

Autor
Gonzalo Barbuto.
Tecnicatura de Desarrollo de Software.
