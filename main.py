from ColaOrdenes import ColaOrdenes
from os import system
from Cliente import Cliente

class Main():
    def __init__(self):
        Cola=ColaOrdenes()
        Opcion=''
        ingrediente=''
        cont=0
        #tiempo=0
        while(Opcion!='5'):
            print('|----- Registro de pedidos -------|')
            print('| 1. Ingresar Orden               |')
            print('| 2. Entregar Orden               |')
            print('| 3. Mostrar Ordenes              |')
            print('| 4. Mostrar Datos del Estudiante |')
            print('| 5. Salir                        |')
            print('|---------------------------------|')
            print('')
            Opcion=input('Seleccione una opción: \n > ')
            if Opcion=='1':
                system('cls')
                print('|    Datos del cliente:    |\n' )
                name=input('Nombres: ')
                apellidos=input('Apellidos: ')
                dpi=input('DPI: ')
                correo=input('Correo: ')
                nuevoCliente=Cliente(name,apellidos,dpi,correo)
                print('\n|    Pizza:    |\n' )
                ingrediente=input('Ingrediente: ')
                if ingrediente.upper()=='PEPPERONI':
                    Cola.agregarOrden(nuevoCliente,ingrediente,3)
                elif ingrediente.upper()=='SALCHICHA':
                    Cola.agregarOrden(nuevoCliente,ingrediente,4)
                elif ingrediente.upper()=='CARNE':
                    Cola.agregarOrden(nuevoCliente,ingrediente,10)
                elif ingrediente.upper()=='QUESO':
                    Cola.agregarOrden(nuevoCliente,ingrediente,5)
                elif ingrediente.upper()=='PIÑA':
                    Cola.agregarOrden(nuevoCliente,ingrediente,2)
                print('\n\n-> Orden agregada\n\n')
               
            elif Opcion=='2':
                pass
                                #if Colapizzas.vacia():
                #    print('Cola Vacía | Órdenes Entregadas: ', Colapizzas.size)
                #    print('')
                #else:
                #    Colapizzas.entregarOrden()
            elif Opcion=='3':
                Cola.mostrarOrdenes()
            elif Opcion=='4':
                system('cls')
                self.DatosEstudiantiles()
        print('Sesión Cerrada\n')
    
    def DatosEstudiantiles(self):
        print(' ')
        print('> Kevin Gerardo Ruíz Yupe ')
        print('> 201903791               ')
        print('> Introducción a la programación y computación 2 sección "C"')
        print('> Ingeniería en Ciencias y Sistemas')
        print('')


s=Main()
