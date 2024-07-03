from Productos.product import Product
from Builder.builder import Builder

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "La parte_1 construida correctamente."

    def build_part2(self):
        self.product.part2 = "La parte_2 construida correctamente."

    def get_product(self):
        return self.product