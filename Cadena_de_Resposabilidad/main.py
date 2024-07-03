
from Cadena_de_Resposabilidad.Cliente.banco import *

def main():
    banco = Banco()
    monto = 134500
    banco.ejecutivo_cuenta.solicitarPrestamo(monto)

if __name__ == "__main__":
    main()