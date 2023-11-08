
#CONCRETE PRODUCT

from formas import Formas

class Cuadrado(Formas):
    def __init__(self, cant_lados):
        super().__init__(cant_lados)

    def get_description(self):
        print("Es un cuadrado")