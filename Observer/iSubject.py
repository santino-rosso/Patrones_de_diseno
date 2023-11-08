from abc import ABCMeta, abstractmethod
from observer import Observer

class ISubject(metaclass=ABCMeta):
    
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass