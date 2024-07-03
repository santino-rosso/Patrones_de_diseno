#CREATOR

from abc import ABCMeta, abstractmethod

class formas (metaclass=ABCMeta):
    @abstractmethod
    def crear_forma(self, cant_lados): #metodo de creacion
        pass