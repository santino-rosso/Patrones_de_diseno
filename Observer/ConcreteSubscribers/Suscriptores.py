from Subscriber.Subscriber import *
from Publisher.Publisher import *

class Suscriptores(Subscriber):
    def __init__(self, subject:Publisher):
        self.subject = subject

    def update(self):
        print("Video publicado!!")
        print(f"Video: {self.subject.get_ultimoVideo()}")