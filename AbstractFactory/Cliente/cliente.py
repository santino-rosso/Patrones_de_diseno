from ConcreteFactory.fabricaAdidas import *
from ConcreteFactory.fabricaNike import *

class Cliente():
    def accion_cliente(self, fabrica):
        zapatillas = fabrica.crear_zapatillas()
        ropa = fabrica.crear_RopaDeportiva()

        print(zapatillas.funcion_zapatillas())
        print(ropa.funcion_ropaDeportiva())