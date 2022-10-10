# Iterators

All the sequences could be run using an structure because they implement the special method ```__iter__```. This method returns an iterator able to run the sequence.

    An iterator is an object that allows to run one by one the elements stored in a data structure. In python the iterators should implement a method NEXT that should return the elemens one by one starting from the begining and in the final element, should show a StopIteration exception.

An iterator is an object used to iterate over iterable objects such as **list, tuples, dictionaries and sets**. An object is called iterable is we can get an iterator from it or loop over it.

A python `iterator object` must implement two specific methods from an iterator protocol:
- __iter__(object, sentinel): Returns an iterator for the supplied object, it generates a thing that can be iterated one element at a time.
    - object: An object whose iterator needs to be created (list, sets, tuples)
    - sentinel (optional): Special value that represents the end of the sequence
- __next__(iterator, defauld): Function that eturns the next item from the iterator. It holds the value *one at a time*
    - iterator: next item from the iterator
    - default (optional): this value is returned if the iterator is exhaused (no next item to retrive) -> StopIteration Exception

    When we use a foor loop to iterate, the exception is handled internally and exploited to terminate the loop. This is one of the distinctions between loops and iterators. When you explicitly call next() you should be prepared to catch the exception yourself

    ```py
    # Program to print the tuple using Iterator protocols
    tup = (87, 90, 100, 500)

    # get an iterator using iter()
    tup_iter = iter(tup)

    # Infinite loop
    while True:
        try:
            # To fetch the next element
            print(next(tup_iter))
            # if exception is raised, break from the loop
        except StopIteration:
            break
    
    ```

## Create our Iterator changing the behavior of buil-in methods iter-next
In this code, we are attempting to implement an iterator of powers of two mannually. In the __iter__() method, we direct the n variable to the initial value. In the __next__() function, we manually increase the n variable to its maximum value
```py
class PowerTwo:
   # Class to implement an iterator of powers of two
   # Constructor accepting the max value
   def __init__(self, max=0):
       self.max = max

   # defined __iter__() to point the first element
   def __iter__(self):
       self.n = 1
       return self

   # __next__() to fetch the next value from the iterator
   def __next__(self):
       if self.n <= self.max:
           result = 2 ** self.n
           self.n += 1
           return result

   # Terminating condition
       else:
           raise StopIteration

# create an object
numbers = PowerTwo(4)

# create an iterable from the object
i = iter(numbers)

# Using for-in loop to print the elements up to max
for it in i:
   print(it)

Output
12
4
8
16
```


# Generators
A generator requires more effort to build because we must create a class containing __iter__() and __next__() but also keep track of internal states.

A `generator`is a function that returns an iterator object with a sucession of values rather than a single item. A `yield`statement, rather than a return statement is used in a generator function

The difference is that, although a return statement terminates a function completely, a `yield`statement pauses the function, save the state and then continues from there on subsquent calls.

## Example: Generator

```py
def topten():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1

values = topten()
for i in values:
    print(i)
```

## Example: Generator for Fibonacci Numbers
Yield can be used as a return statement. In this case, the above function returns a generator that can be iterated upon insted of eturning the ouput when done so. Python iterates over the code until it reaches a yield line within the function. The function then transmits the produced value and pauses in that state without leaving. When the function is called again, its last paused state is remembered, and execution is begun from there. This will continue until the generator is exhausted. 

```py
# A simple generator for Fibonacci Numbers
def fib(max):
   # Initialize first two Fibonacci Numbers
   p, q = 0, 1

   # yield next Fibonacci Number one at a time
   while p < max:
       yield p
       p, q = q, p + q

# Ask the user to enter the maximum number
n = int(input("Enter the number up to which you wish the Fibonacci series to be printed: \n"))

# Create a generator object
x = fib(n)
# Iterating over the generator object using for
# in a loop.
print("Resultant Series up to", n, "is :")
for i in x:
   print(i)

Output
Resultant Series up to 5 is :
0
1
1
2
3
```

Why use generators when the return statement is already present?

The most well-known feature of generators is their excellent memory efficiency. A standard function that returns a sequence will first construct the whole sequence in memory before returning the result. If the number of elements in the sequence is enormous, this is overkill. The generator implementation of such sequences, on the other hand, is memory-friendly and preferable since it only generates one item at a time.