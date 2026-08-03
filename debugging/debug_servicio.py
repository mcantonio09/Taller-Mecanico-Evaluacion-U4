import sys
import os
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)
from CRUD.ControladorServicios import ControladorServicios

def probar_depuracion():
    print("--- INICIANDO PRUEBA DE DEBUGGING CON PDB ---")
    controlador = ControladorServicios()
    cliente_prueba = "Rocio Garcia"
    vehiculo_prueba = "Suzuki Swift"
    tipo_prueba = "Mantenimiento 30000 km"
    costo_prueba = 2900.0

    print("Punto crítico alcanzado. A continuación se detendrá la ejecución:")
    breakpoint()
    resultado = controlador.registrar_servicio(cliente_prueba, vehiculo_prueba, tipo_prueba, costo_prueba)
    print(f"Resultado obtenido: {resultado}")

if __name__ == "__main__":
    probar_depuracion()