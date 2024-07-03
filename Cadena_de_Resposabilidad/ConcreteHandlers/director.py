from Cadena_de_Resposabilidad.Handler.iAprobador import *

class Director(IAprobador):

    def __init__(self):
        self._next = None
    
    def set_next(self, next):
        self._next = next
    
    def solicitarPrestamo(self, monto):
        if monto > 10000:
            print("El Director maneja la solicitud del prestamo")
        else:
            self._next.solicitarPrestamo(monto)