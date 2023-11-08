#CREATOR

from abc import ABCMeta, abstractmethod

class IFormas (metaclass=ABCMeta):
    @abstractmethod
    def crear_forma(self, cant_lados): #metodo de creacion
        pass