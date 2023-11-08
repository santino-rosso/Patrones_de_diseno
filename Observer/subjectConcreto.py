from iSubject import ISubject
from observer import Observer

class CanalYouTube(ISubject):
    def __init__(self):
        self.suscriptores=[]
        self.ulitimoVideo = ""

    #agrego suscriptores
    def attach(self, observer):
        self.suscriptores.append(observer)
           
    #eliminar suscriptor
    def detach(self, observer: Observer):
        a = -1
        for s in self.suscriptores:
            a += 1
            if s == observer:
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
    
