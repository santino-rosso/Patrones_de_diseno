from ConcretePublisher.CanalYouTube import *
from ConcreteSubscribers.Suscriptores import *

def main():
    canal = CanalYouTube()
    suscriptor1 = Suscriptores(canal)
    suscriptor2 = Suscriptores(canal)

    canal.attach(suscriptor1)
    canal.attach(suscriptor2)
    
    canal.agregarVideo("Aprendiendo el patron Observer")
    #canal.detach(suscriptor2)
    canal.detach(suscriptor1)

    

if __name__ == "__main__":
    main()