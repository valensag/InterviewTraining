"""
x = range(1,10)
print(type(x))

def iterator():
    for i in x:
        yield i

print(iterator())

dictionary = {i: 5+i for i in range(1,10)}
print(dictionary)
"""

dictionary = {i+1: chr(ord("a")+i) for i in range(0,10)}
print(dictionary)
