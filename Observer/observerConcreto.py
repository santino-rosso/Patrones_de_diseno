from observer import *
from iSubject import *

class Suscriptores(Observer):
    def __init__(self, subject:ISubject):
        self.subject = subject

    def update(self):
        print("Video publicado!!")
        print(f"Video: {self.subject.get_ultimoVideo()}")