from Publisher.Publisher import Publisher
from Subscriber.Subscriber import Subscriber

class CanalYouTube(Publisher):
    def __init__(self):
        self.suscriptores=[]
        self.ulitimoVideo = ""

    #agrego suscriptores
    def attach(self, subscriber):
        self.suscriptores.append(subscriber)
           
    #eliminar suscriptor
    def detach(self, subscriber: Subscriber):
        a = -1
        for s in self.suscriptores:
            a += 1
            if s == subscriber:
                self.suscriptores.pop(a)
                print(f"Elimnado suscriptor numero {a}")
    
    def notify(self):
        for s in self.suscriptores:
            s.update()
    
    def agregarVideo(self, titulo):
        self.ulitimoVideo=titulo
        print("Nuevo video agregado al canal")
        self.notify()
        

    def get_ultimoVideo(self):
        return self.ulitimoVideo
    
