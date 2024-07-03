#ABSTRACT PRODUCT A
from abc import ABCMeta, abstractmethod


class Zapatillas(metaclass=ABCMeta):
    @abstractmethod
    def funcion_zapatillas(self):
        pass