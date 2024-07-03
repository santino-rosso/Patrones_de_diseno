from Cadena_de_Resposabilidad.Handler.iAprobador import *

class EjecutivoCuentas(IAprobador):

    def __init__(self):
        self._next = None
    
    def set_next(self, next):
        self._next = next
    
    def solicitarPrestamo(self, monto):
        if monto <= 10000:
            print("El Ejecutivo de Cuenta maneja la solicitud del prestamo")
        else:
            self._next.solicitarPrestamo(monto)
        