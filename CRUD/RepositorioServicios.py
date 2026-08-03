import mysql.connector
from mysql.connector import Error
from Servicio import Servicio

class RepositorioServicios:
    def __init__(self, host="localhost", user="root", password="Litiid015*", database="db_taller"):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def _conectar(self):
        return mysql.connector.connect(**self.config)

    def registrar(self, servicio):
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            query = "INSERT INTO servicios (cliente, vehiculo, tipo_servicio, costo) VALUES (%s, %s, %s, %s)"
            valores = (servicio.cliente, servicio.vehiculo, servicio.tipo_servicio, servicio.costo)
            cursor.execute(query, valores)
            conexion.commit()
            
        except Error as e:
            print(f"Error de base de datos al registrar: {e}")
            raise BaseException("Error al guardar en la base de datos.")
            
        else:
            id_generado = cursor.lastrowid
            servicio.id_servicio = id_generado
            return servicio
            
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    def obtener_todos(self):
        conexion = None
        servicios_lista = []
        try:
            conexion = self._conectar()
            cursor = conexion.cursor(dictionary=True) # dictionary=True devuelve las filas como diccionarios
            cursor.execute("SELECT * FROM servicios")
            filas = cursor.fetchall()
            
            for fila in filas:
                obj_servicio = Servicio(
                    id_servicio=fila['id'],
                    cliente=fila['cliente'],
                    vehiculo=fila['vehiculo'],
                    tipo_servicio=fila['tipo_servicio'],
                    costo=fila['costo']
                )
                servicios_lista.append(obj_servicio)
                
        except Error as e:
            print(f"Error al consultar servicios: {e}")
            
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()
                
        return servicios_lista

    def actualizar(self, servicio):
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            query = """UPDATE servicios 
                       SET cliente = %s, vehiculo = %s, tipo_servicio = %s, costo = %s 
                       WHERE id = %s"""
            valores = (servicio.cliente, servicio.vehiculo, servicio.tipo_servicio, servicio.costo, servicio.id_servicio)
            cursor.execute(query, valores)
            conexion.commit()
            
        except Error as e:
            print(f"Error al actualizar: {e}")
            
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()

    def eliminar(self, id_servicio):
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM servicios WHERE id = %s", (id_servicio,))
            conexion.commit()
            
            if cursor.rowcount == 0:
                raise ValueError(f"No se encontró el servicio con ID {id_servicio}")
                
        except Error as e:
            print(f"Error al eliminar: {e}")
            raise e
            
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()