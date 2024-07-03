
#CONCRETE PRODUCT

from Product.IFormas import IFormas

class Cuadrado(IFormas):
    def __init__(self, cant_lados):
        super().__init__(cant_lados)

    def get_description(self):
        print("Es un cuadrado")