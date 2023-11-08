#handler
from abc import ABCMeta, abstractmethod

class IAprobador(metaclass = ABCMeta):

    @abstractmethod
    def set_next(self):
        pass

    @abstractmethod
    def solicitarPrestamo(self,monto):
        pass