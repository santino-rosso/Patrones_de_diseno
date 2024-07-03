from abc import ABCMeta, abstractmethod
from Subscriber.Subscriber import Subscriber

class Publisher(metaclass=ABCMeta):
    
    @abstractmethod
    def attach(self, subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber: Subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass