#CONCRETE CREATOR

from cuadrado import Cuadrado
from pentagono import Pentagono
from triangulo import Triangulo
from iFormas import *

class FactoryMethod(IFormas):

    def crear_forma(self, cant_lados):
        if cant_lados == 3:
            return Triangulo(cant_lados)
        elif cant_lados == 4:
            return Cuadrado(cant_lados)
        elif cant_lados == 5:
            return Pentagono(cant_lados)
