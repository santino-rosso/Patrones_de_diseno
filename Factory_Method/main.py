from ConcreteCreator.factoryMethod import FactoryMethod

def main():
    factory=FactoryMethod()
    forma = factory.crear_forma(3)
    forma.get_description()

if __name__=="__main__":
    main()