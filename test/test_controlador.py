import pytest
from unittest.mock import MagicMock
from CRUD.ControladorServicios import ControladorServicios
from exceptions.excepciones import CostoInvalidoError

def test_registrar_servicio_costo_invalido():
    controlador = ControladorServicios()
    controlador.repositorio = MagicMock() 
  
    cliente = "Mario Garcia"
    vehiculo = "Nissan Versa"
    tipo = "Cambio de aceite"
    costo_negativo = -150.0

    with pytest.raises(CostoInvalidoError) as error_info:
        controlador.registrar_servicio(cliente, vehiculo, tipo, costo_negativo)
        
    assert "El costo del servicio debe ser mayor a 0" in str(error_info.value)


def test_registrar_servicio_costo_no_numerico():
    controlador = ControladorServicios()
    controlador.repositorio = MagicMock()
    
    with pytest.raises(ValueError) as error_info:
        controlador.registrar_servicio("Roberto Moreno", "Kia Rio", "Frenos", "cuatrocientos veinte pesos")
        
    assert "El costo debe ser un valor numérico" in str(error_info.value)


def test_registrar_servicio_exitoso():
    controlador = ControladorServicios()
    mock_repo = MagicMock()
    
    mock_repo.registrar.return_value = "Registro Exitoso" 
    controlador.repositorio = mock_repo
    
    resultado = controlador.registrar_servicio("Antonio Moreno", "Toyota Corolla", "Servicio 20000 km", 2500)
    
    mock_repo.registrar.assert_called_once()
    assert resultado == "Registro Exitoso"