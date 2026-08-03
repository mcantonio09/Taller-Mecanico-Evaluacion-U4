class Servicio:
    def __init__(self, cliente, vehiculo, tipo_servicio, costo, id_servicio=None):
        self.id_servicio = id_servicio
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.tipo_servicio = tipo_servicio
        self.costo = costo

    def __str__(self):
        return f"Servicio[{self.id_servicio}]: {self.cliente} - {self.vehiculo} | {self.tipo_servicio} | ${self.costo}"