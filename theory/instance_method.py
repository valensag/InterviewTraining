import logging

logging.basicConfig(level=logging.INFO)
class Calculator:


    def __init__(self, version: int):
        self.version = version
    
    #This is an instance method because it works with the Self that is the instance
    #This does not depend of abstract args but should be inside the class
    def description(self):
        logging.info(f"Calculator version is {self.version}")

    #Can go out of the class, it doesn work with self
    @staticmethod
    def add_numbers(*numbers:float):
        logging.info(f"Numbers: {numbers}")


if __name__ == '__main__':
    calculator1 = Calculator(1)
    calculator1.description()
    calculator2 = Calculator(2)
    calculator2.description()
    calculator2.add_numbers(10,11)