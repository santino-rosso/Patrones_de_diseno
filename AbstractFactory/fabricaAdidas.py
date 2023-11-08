#CONCRETE FACTORY 2
from fabrica import Fabrica
from adidasRopaDeportiva import RopaDeportivaAdidas
from adidasZapatillas import ZapatillasAdidas

class FabricaAdidas(Fabrica):

    def crear_RopaDeportiva(self):
        return RopaDeportivaAdidas()
        
    def crear_zapatillas(self):
        return ZapatillasAdidas()