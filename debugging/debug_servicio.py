import sys
import os

# Configuramos las rutas para poder importar desde la carpeta CRUD
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from CRUD.ControladorServicios import ControladorServicios

def probar_depuracion():
    print("--- INICIANDO PRUEBA DE DEBUGGING CON PDB ---")
    controlador = ControladorServicios()
    
    cliente_prueba = "Roberto Gomez"
    vehiculo_prueba = "Nissan Sentra"
    tipo_prueba = "Cambio de balatas"
    costo_prueba = 1200.0

    print("Punto crítico alcanzado. A continuación se detendrá la ejecución:")
    
    # AQUÍ INSERTAMOS EL DEBUGGER (Equivalente a pdb.set_trace())
    breakpoint()
    
    # Esta línea se ejecutará cuando le des la orden al debugger
    resultado = controlador.registrar_servicio(cliente_prueba, vehiculo_prueba, tipo_prueba, costo_prueba)
    print(f"Resultado obtenido: {resultado}")

if __name__ == "__main__":
    probar_depuracion()