# Object Oriented Programming

In the real world we interact with ````Objects````, if I need to make a call I use the phone, I need to search information I use a computer, if I enter in a company, I will found other employees there. Every object will have ```attributes```(properties) -> ***variables*** and ```behavior```(actions) -> ***methods*** 

In the real world we have phones that are manufactured around the world, there are thousand of millions of the same phone for example the xiaomy T3 PRO but there is only one desing, in OPP the design is ```the class```, it's a blueprint.

So before creating an object, we need to create a class, because is the desing of that object.
- One class can have millions of objects but the behavior will depends of the object
- ```Self``` is the object that you are passing and is a constructor

```py
class Computer:
    #Special Method __init__ used to initialize the variables.
    #Called automatically, we pass those arguments (self, cpu, ram)
    
    def __init__(self, cpu, ram):
        #We need to asign those attributes for our object, so we use self
        self.cpu = cpu
        self.ram = ram
        

    def config(self):
        #Here we are binding our data with our objects
        print("Config is: ", self.cpu, self.ram)

#Create an instance of the class and call method __init__
#Remembe we are passing 3 args (pc1, cpu, ram)
pc1 = Computer('i5', 16)
pc2 = Computer('Ryzen 3', 8)

pc1.config()
pc2.config()
```

- In the computer we have something called ***Heap Memory*** is where we store all our objects, and this will have an address. Every time you create an object it will have a different address. The size of this stored object will depends by the amount and size of the arguments that you are passing. And the responsable to calculate this size is the ```Constructor```.
- ```Self``` is the pointer to the specific object and is very important because with this we can change the properties and behavior of an specific object


## Variable Types
1. ```Instance variable: ``` Are the variables defined inside the __init__
2. ```Class (Static) variable: ``` We use this when we want to create a variable that is common for all the objects. We have to define them before the __init__.

    If you want to change this class variable, you will need to call the class like this: ```Car.Wheels = 5``` because we need to enter in the ```Class namespace```
    - **Namespace:** Is an area where you create and store object/variable
        - *Class namespace:*
        - *Object / Instance namespace:*
    ```py
    class Car:
        wheels = 4

        def __init__(self):
            self.mil = 10
            self.com = "BMW"
    
    c1 = Car()
    c2 = Car()

    Car.Wheels = 5
    ```

## Methods Types
1. ```Instance methods: ``` It's a method where we pass *self*, it means that it belongs to a particular object.
    ## Instance methods types
    - Accessor Methods -> get
    - Mutator Methods -> set
2. ```Class methods: ``` They can use class variables, and we also use a special symbol called ***Decorator*** -> ***@classmethod***
3. ```Static methods: ``` If we need a method that doesn't work with class and instance variables, we use a *static method*, and we also use a special symbol called ***Decorator*** -> ***@staticmethod***

```py
class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #Instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    #Instance method accessor
    def get_m1(self):
        return self.m1

    #Instance method mutator
    def set_m1(self, value):
        self.m1 = value

    #Class method with the decorator that pass the cls
    @classmethod
    def getSchool(cls):
        print cls.school

    @staticmethod
    def info():
        print("This is Student class... in abc module)

s1 = Student(34,47,32)
s2 = Student(89,32,12)

#Call instance method
print(s1.avg())

#Call class method
print(Student.getSchool())

#Call static method
Student.info()

```


## Inner Class

When we need to create a class inside a class. We instance the inner class inside the constructor on init method of the class or you can create an object of inner class outside the outer class providing the class name to call it

```py
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

```


# 4 Pillars


- **Encaptulation**: Reduce the complexity and increase reausability
- **Abstraction**: Reduce complexity and isolate impact of changes
- **Inheritance**: Eliminate redundant code
- **Polymorphism**: Refactor ugly statements 

Before we use to have the Procedual Programming, that divide a program in a set of functions, the data was stored in a bunch of variables and a function that operate on the data. This method is not recommended because you will have to repeat a lot of code and you will need to start changing the behavior of the function when the complexity and amount of functions start to growth. There is a lot of interdependency between this functions, this was called spagetti code.

In ```OOP``` we group variables and functions into a unit and we call that unit an ```object```. These variables are ```properties``` and the functions are ```methods```

An example could be a Car, that have properties like make, model and color. And have methods like start(), stop(), move()

    In OPP we group related variables and functions that operate on them into objects and this is what we call ENCAPTULATION



# Encaptulation
## Procedural Programming example
```py
#In this example the functions depends of many variables
baseSalary = 30_000
overtime = 10
rate = 20

def getWage(baseSalary, overtime, rate):
    return baseSalary + (overtime*rate)

```

# OOP Programming example with ```Encaptulation````

def class 

# Abstraction
We have many complex objects in the real world, but we can abstract only the properties and functions that we need, hidding the others and making the interface of those objects ```simpler``` and also ```reduce the Impact of Change```

# Inheritance
Mechanism that allows you to eliminate redundant code
In real life, there is a relation between parents and childs, everythings that belongs to the parent also belongs to the child

- Single level Inheritance
- Multi level Inheritance
- Multi Inheritance
- MRO --> Order of Inheritance (left to right)



# Polymorphism
```One thing can take multiple forms``` 

Is very important to loose coupling, create interfaces, reduce dependency injections.
## 1. Duck Typing:
If a bierd walks as a duck, sings as a duck and swim as a duck, it should be a duck

## 2. Operator Overloading 
Operators (+, - ,/ ), behind the sean you are calling a Magic methods (__add__, __sub__, __mul__)
```py
a = 5
b = 2
print(a+b)
print(int.__add__(a,b))

```
## 3. Method Overloading 
Two methods with the same name but different amount of arguments
## 4. Method Overriding
Two methods with same name and number of arguments but inside a inheritance




