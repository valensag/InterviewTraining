class Student:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.laptop = self.Laptop()
    
    def show(self):
        print(self.name, self.lastname)
        self.laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)


s1 = Student('Navin', 'Ramirez')
s2 = Student('Jenny', 'Lopez')
s1.show()
s2.show()