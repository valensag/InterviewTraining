# Clases

We can create data classes using classes, we can create our own data type

`Example:` A class is a cookie cutter

- `def __init__(self, parameter)`: This is a constructor.
- If a method has `self` in there, it is a method that is part of the class
- `parameter`: the parameter will be applied to the specific instance that we create with the class

```py
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = 'yellow'

cookie1 = Cookie('green')
cookie2 = Cookie('blue')

print(f"cookie 1: {cookie1.get_color()}")
print(f"cookie 2: {cookie2.get_color()}")

cookie2.set_color("yellow")

print(f"cookie 1 updated: {cookie1.get_color()}")
print(f"cookie 2 updated: {cookie2.get_color()}")
-----------------------------
cookie 1: green
cookie 2: blue
cookie 1 updated: green
cookie 2 updated: yellow
```

# Pointers

Works different depending the data type

- Integers: Inmutable after created, you can't change the node that they are pointing after the creation

```py
num1 = 1
num2 = num1

print('Before')
print(f"num1: {num1} id: {id(num1)}")
print(f"num2: {num2} id: {id(num2)}")

num2 = 12
print('After')
print(f"num1: {num1} id: {id(num1)}")
print(f"num2: {num2} id: {id(num2)}")
----------------------------
Before
num1: 1 id: 4377174632
num2: 1 id: 4377174632
After
num1: 1 id: 4377174632
num2: 12 id: 4377174984

```

At the beginning, they are pointing to the same memory, then we change the value of num2 and num1 didn't change

- Dicitionaries: Mutable, we can change the space in memory that the variable is pointing but

```py
dict1 = {'value':2}
dict2 = dict1

print('Before')
print(f"dict1: {dict1} id: {id(dict1)}")
print(f"dict2: {dict2} id: {id(dict2)}")

dict2['value'] = 40
print('After')
print(f"dict1: {dict1} id: {id(dict1)}")
print(f"dict2: {dict2} id: {id(dict2)}")
-----------------------------------------
Before
dict1: {'value': 2} id: 4348101376
dict2: {'value': 2} id: 4348101376
After
dict1: {'value': 40} id: 4348101376
dict2: {'value': 40} id: 4348101376

```

Notice that here actualy the space in memory of dict1 value changed even if the dict2 was the only one changed
