class Orden:
    def __init__(self,Cliente,ingrediente,tiempo):
        self.Cliente=Cliente
        self.ingrediente=ingrediente
        self.tiempo=tiempo
        self.siguiente=None
