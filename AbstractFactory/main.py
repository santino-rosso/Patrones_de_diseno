from Cliente.cliente import *

def main():
    c = Cliente()
    print("---FABRICA NIKE---")
    c.accion_cliente(FabricaNike())

    print("\n---FABRICA ADIDAS---")
    c.accion_cliente(FabricaAdidas())

if __name__=="__main__":
    main()