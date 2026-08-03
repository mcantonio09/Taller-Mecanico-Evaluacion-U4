# Sistema CRUD - Taller Mecánico

## Descripción
Módulo principal del sistema de gestión para el taller mecánico, desarrollado bajo principios SOLID y Programación Orientada a Objetos (POO).

## Estructura de Clases
- **Servicio:** Entidad de datos (DTO) que almacena la información (ID, cliente, vehículo, tipo de servicio, costo).
- **RepositorioServicios:** Capa de persistencia encargada exclusivamente de la conexión y operaciones con MySQL.
- **ControladorServicios:** Lógica de negocio y validaciones.
- **Interfaz:** Vista gráfica construida con Tkinter.

## Configuración y Ejecución
1. Asegúrate de tener instalado Python y la librería de MySQL:
   pip install mysql-connector-python

2. Ejecuta el script SQL db_taller.sql en tu servidor MySQL para crear la base de datos y la tabla.

3. Ingresa tu contraseña de tu MySQL para el ingreso en la base de datos del modulo RepositorioServicios Linea 6 "password" 

3. Ejecuta la aplicación desde la raíz del proyecto con el archivo main.py:
    python main.py
