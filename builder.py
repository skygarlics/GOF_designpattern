import abc


"""
Example of string builder
"""

class Director:
    """
    construct object using Builder interface
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()


class Builder(metaclass=abc.ABCMeta):
    """
    specify abstract interface for Product object
    """

    def __init__(self):
        self.product = Product()

    def get_product(self):
        return self.product

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass


class Builder1(Builder):
    """
    concrete builder
    """

    def _build_part_a(self):
        self.product += "Part A\n"

    def _build_part_b(self):
        self.product += "Part B\n"


class Product:
    """
    Complex object
    """

    def __init__(self):
        self._str = ""

    def __add__(self, X):
        return self._str + X

    def __str__(self):
        return self._str


def main():
    builder1 = Builder1()
    director = Director()
    director.construct(builder1)
    product = builder1.product
    print(product)

if __name__ == "__main__":
    main()
