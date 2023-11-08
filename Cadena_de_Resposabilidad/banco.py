from ejecutivo_cuenta import *
from liderTeamEjecutivo import *
from gerente import *
from director import *

class Banco():
    def __init__(self):
        self.ejecutivo_cuenta = EjecutivoCuentas()
        self.liderTeamEjecutivo = LiderTeamEjecutivo()
        self.gerente = Gerente()
        self.director = Director()
        
        self.ejecutivo_cuenta.set_next(self.liderTeamEjecutivo)
        self.liderTeamEjecutivo.set_next(self.gerente)
        self.gerente.set_next(self.director)