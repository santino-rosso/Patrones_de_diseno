#CONCRETE CREATOR

from ConcreteProducts.cuadrado import Cuadrado
from ConcreteProducts.pentagono import Pentagono
from ConcreteProducts.triangulo import Triangulo
from Creator.formas import *

class FactoryMethod(formas):

    def crear_forma(self, cant_lados):
        if cant_lados == 3:
            return Triangulo(cant_lados)
        elif cant_lados == 4:
            return Cuadrado(cant_lados)
        elif cant_lados == 5:
            return Pentagono(cant_lados)
