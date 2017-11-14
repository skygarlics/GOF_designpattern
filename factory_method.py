import abc

class Creator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def factoryMethod(self):
        pass

    def operation(self):
        self.product = self.factoryMethod()


class Creator1(Creator):

    def factoryMethod(self):
        return Product1()


class Product(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def work(self):
        pass


class Product1(Product):
    def work(self):
        pass

    def __str__(self):
        return "Product 1"



def main():
    creator1 = Creator1()
    creator1.operation()
    print(creator1.product)

if __name__ == "__main__":
    main()
