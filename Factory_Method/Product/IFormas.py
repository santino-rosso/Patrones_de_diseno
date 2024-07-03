#PRODUCT(INTERFAZ)

from abc import ABCMeta, abstractmethod

class IFormas(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, cant_lados):
        self.cant_lados = cant_lados
    
    @abstractmethod
    def get_description(self):
        pass