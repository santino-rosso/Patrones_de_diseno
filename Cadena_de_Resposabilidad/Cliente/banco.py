from Cadena_de_Resposabilidad.ConcreteHandlers.ejecutivo_cuenta import *
from Cadena_de_Resposabilidad.ConcreteHandlers.liderTeamEjecutivo import *
from Cadena_de_Resposabilidad.ConcreteHandlers.gerente import *
from Cadena_de_Resposabilidad.ConcreteHandlers.director import *

class Banco():
    def __init__(self):
        self.ejecutivo_cuenta = EjecutivoCuentas()
        self.liderTeamEjecutivo = LiderTeamEjecutivo()
        self.gerente = Gerente()
        self.director = Director()
        
        self.ejecutivo_cuenta.set_next(self.liderTeamEjecutivo)
        self.liderTeamEjecutivo.set_next(self.gerente)
        self.gerente.set_next(self.director)