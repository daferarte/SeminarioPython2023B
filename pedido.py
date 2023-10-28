class Usuarios:

    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido= apellido
        self.cedula = cedula

    def RealizarPedido(self, telefono, direccion, pedido):
        self.telefono = telefono
        self.direccion = direccion


class pedido:

    def __init__(self, plato, fecha="hoy"):
        self.plato=plato