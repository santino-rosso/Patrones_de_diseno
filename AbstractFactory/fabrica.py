#ABSTRACT FACTORY

from abc import ABCMeta, abstractmethod

class Fabrica(metaclass=ABCMeta):

    @abstractmethod
    def crear_zapatillas(self):
        pass

    @abstractmethod
    def crear_RopaDeportiva(self):
        pass
