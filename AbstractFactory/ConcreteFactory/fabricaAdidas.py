#CONCRETE FACTORY 2
from AbstracFactory.fabrica import Fabrica
from ConcreteProducts.adidasRopaDeportiva import RopaDeportivaAdidas
from ConcreteProducts.adidasZapatillas import ZapatillasAdidas

class FabricaAdidas(Fabrica):

    def crear_RopaDeportiva(self):
        return RopaDeportivaAdidas()
        
    def crear_zapatillas(self):
        return ZapatillasAdidas()