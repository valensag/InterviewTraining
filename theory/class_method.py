from datetime import date
import logging

logging.basicConfig(level=logging.INFO)

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def description(self):
        logging.info(f"The person {self.name} is {self.age} years old")

    @classmethod
    def get_age_by_year(cls, name:str, year: int):
        #Create a factory or an alternative constructor of init
        current_year:int = date.today().year
        age:int = current_year-year
        return cls(name,age)
    
if __name__ == '__main__':
    valentina = Person.get_age_by_year("Valentina", 1997)
    valentina.description()
        


