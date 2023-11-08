#CONCRETE FACTORY 1
from fabrica import Fabrica
from nikeRopaDeportiva import *
from nikeZapatillas import *

class FabricaNike(Fabrica):

    def crear_zapatillas(self):
        return ZapatillasNike()

    def crear_RopaDeportiva(self):
        return RopaDeportivaNike()