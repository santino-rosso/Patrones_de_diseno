from Cadena_de_Resposabilidad.Handler.iAprobador import *

class LiderTeamEjecutivo(IAprobador):

    def __init__(self):
        self._next = None
    
    def set_next(self, next):
        self._next = next
    
    def solicitarPrestamo(self, monto):
        if monto > 10000 and monto <= 50000:
            print("El Lider Team Ejecutivo maneja la solicitud del prestamo")
        else:
            self._next.solicitarPrestamo(monto)