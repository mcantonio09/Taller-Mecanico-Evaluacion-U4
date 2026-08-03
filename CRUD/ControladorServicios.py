import sys
import os

# 1. Obtenemos la ruta absoluta de la carpeta principal del proyecto (un nivel arriba de /CRUD)
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2. Agregamos esa ruta al "Path" del sistema para que Python busque ahí
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

# 3. Ahora sí, importamos desde la carpeta 'exceptions' el archivo 'excepciones.py'
from exceptions.excepciones import CostoInvalidoError, ServicioNoEncontradoError

from Servicio import Servicio
from RepositorioServicios import RepositorioServicios

class ControladorServicios:
    def __init__(self):
        self.repositorio = RepositorioServicios()

    def registrar_servicio(self, cliente, vehiculo, tipo_servicio, costo):
        try:
            costo_float = float(costo)
        except ValueError:
            raise ValueError("El costo debe ser un valor numérico.")

        if costo_float <= 0:
            raise CostoInvalidoError(costo_float)

        nuevo_servicio = Servicio(cliente, vehiculo, tipo_servicio, costo_float)
        return self.repositorio.registrar(nuevo_servicio)

    def obtener_servicios(self):
        return self.repositorio.obtener_todos()

    def actualizar_servicio(self, id_servicio, cliente, vehiculo, tipo_servicio, costo):
        try:
            costo_float = float(costo)
        except ValueError:
            raise ValueError("El costo debe ser un valor numérico.")

        if costo_float <= 0:
            raise CostoInvalidoError(costo_float)

        servicio_actualizado = Servicio(cliente, vehiculo, tipo_servicio, costo_float, id_servicio)
        self.repositorio.actualizar(servicio_actualizado)
        return servicio_actualizado

    def eliminar_servicio(self, id_servicio):
        try:
            self.repositorio.eliminar(id_servicio)
        except ValueError:
            raise ServicioNoEncontradoError(id_servicio)