import abc

class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare interface
    """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Implement create concrete product
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Implement create concrete product
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Declare interface of product A
    """

    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Define product object
    """

    def interface(self):
        print("ConcreteProductA1")


class ConcreteProductA2(AbstractProductA):
    """
    Define product object
    """

    def interface(self):
        print("ConcreteProductA2")


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    Declare Interface of product B
    """

    @abc.abstractmethod
    def interface(self):
        pass


class ConcreteProductB1(AbstractProductB):
    """
    Define product object
    """

    def interface(self):
        print("ConcreteProductB1")


class ConcreteProductB2(AbstractProductB):
    """
    Define product object
    """

    def interface(self):
        print("ConcreteProductB2")


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface()
        product_b.interface()

if __name__ == "__main__":
    main()
