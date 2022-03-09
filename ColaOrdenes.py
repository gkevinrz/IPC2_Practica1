
from orden import Orden
class ColaOrdenes:
    def __init__(self):
        self.primero=None
        self.size=0
    
    def agregarOrden(self,Cliente,ingrediente,time):
        if self.primero is None:
            nuevaOrden=Orden(Cliente,ingrediente,time)
            self.primero=nuevaOrden
            self.size+=1
        else:
            temp=self.primero
            ti=temp.tiempo
            while temp.siguiente is not None:
                temp=temp.siguiente
                ti+=temp.tiempo
            ti=ti+time
            nuevaOrden2=Orden(Cliente,ingrediente,ti)
            temp.siguiente=nuevaOrden2

    '''def entregarOrden(self):
        tempo=self.primero
        while tempo is not None:
            print(f'Pizza de {self.primero.Ingrediente} entregada\n')
            self.primero=self.primero.siguiente
            tempo=self.primero
            break

    def vacia(self):
        if self.primero is None:
            return True
        return False'''

        
    def mostrarOrdenes(self):
        tempo = self.primero
        texto=''
        while tempo is not None:
            texto+=f'Cliente {tempo.Cliente.Nombres} | Pizza de: {tempo.ingrediente} - Lista en: {tempo.tiempo} minutos\n'
            tempo = tempo.siguiente
        print(texto)
