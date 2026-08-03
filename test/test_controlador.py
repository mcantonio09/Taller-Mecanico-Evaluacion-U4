import pytest
from unittest.mock import MagicMock

# Importaciones absolutas desde la raíz del proyecto
from CRUD.ControladorServicios import ControladorServicios
from exceptions.excepciones import CostoInvalidoError

# --- PRUEBAS UNITARIAS (PATRÓN AAA) ---
def test_registrar_servicio_costo_invalido():
    """
    Prueba que el sistema rechace un costo negativo o cero.
    """
    # 1. Arrange (Preparar)
    # ... resto de tu código ...
# --- PRUEBAS UNITARIAS (PATRÓN AAA) ---

def test_registrar_servicio_costo_invalido():
    """
    Prueba que el sistema rechace un costo negativo o cero.
    """
    # 1. Arrange (Preparar)
    controlador = ControladorServicios()
    # "Burlamos" (Mock) el repositorio para no conectar a MySQL real
    controlador.repositorio = MagicMock() 
    
    cliente = "Juan Pérez"
    vehiculo = "Toyota Corolla"
    tipo = "Cambio de aceite"
    costo_negativo = -150.0

    # 2 y 3. Act & Assert (Actuar y Afirmar)
    # Verificamos que pytest capture el error exacto que definimos
    with pytest.raises(CostoInvalidoError) as error_info:
        controlador.registrar_servicio(cliente, vehiculo, tipo, costo_negativo)
        
    # Afirmamos que el mensaje de error contiene el texto esperado
    assert "El costo del servicio debe ser mayor a 0" in str(error_info.value)


def test_registrar_servicio_costo_no_numerico():
    """
    Prueba que el sistema rechace un texto cuando se espera un número en el costo.
    """
    # 1. Arrange (Preparar)
    controlador = ControladorServicios()
    controlador.repositorio = MagicMock()
    
    # 2 y 3. Act & Assert (Actuar y Afirmar)
    with pytest.raises(ValueError) as error_info:
        controlador.registrar_servicio("Ana", "Honda Civic", "Frenos", "letras_en_vez_de_numeros")
        
    assert "El costo debe ser un valor numérico" in str(error_info.value)


def test_registrar_servicio_exitoso():
    """
    Prueba que la lógica fluya correctamente con datos válidos.
    """
    # 1. Arrange (Preparar)
    controlador = ControladorServicios()
    mock_repo = MagicMock()
    
    # Simulamos que el repositorio devuelve un mensaje de éxito al guardar
    mock_repo.registrar.return_value = "Registro Exitoso" 
    controlador.repositorio = mock_repo
    
    # 2. Act (Actuar)
    resultado = controlador.registrar_servicio("Carlos", "Ford Fiesta", "Alineación", 500)
    
    # 3. Assert (Afirmar)
    # Verificamos que se haya llamado al método registrar del repositorio simulado
    mock_repo.registrar.assert_called_once()
    assert resultado == "Registro Exitoso"