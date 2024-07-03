#CONCRETE FACTORY 1
from AbstracFactory.fabrica import Fabrica
from ConcreteProducts.nikeRopaDeportiva import *
from ConcreteProducts.nikeZapatillas import *

class FabricaNike(Fabrica):

    def crear_zapatillas(self):
        return ZapatillasNike()

    def crear_RopaDeportiva(self):
        return RopaDeportivaNike()