from Cadena_de_Resposabilidad.Handler.iAprobador import *

class Gerente(IAprobador):

    def __init__(self):
        self._next = None
    
    def set_next(self, next):
        self._next = next
    
    def solicitarPrestamo(self, monto):
        if monto > 50000 and monto <=100000:
            print("El Gerente maneja la solicitud del prestamo")
        else:
            self._next.solicitarPrestamo(monto)