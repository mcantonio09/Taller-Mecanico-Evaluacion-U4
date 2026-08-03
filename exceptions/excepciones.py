class ServicioNoEncontradoError(Exception):
    def __init__(self, id_servicio, mensaje="El servicio solicitado no existe en los registros."):
        self.id_servicio = id_servicio
        self.mensaje = f"Error con ID {id_servicio}: {mensaje}"
        super().__init__(self.mensaje)

class CostoInvalidoError(Exception):
    def __init__(self, costo, mensaje="El costo del servicio debe ser mayor a 0."):
        self.costo = costo
        self.mensaje = f"Costo ingresado (${costo}) inválido. {mensaje}"
        super().__init__(self.mensaje)