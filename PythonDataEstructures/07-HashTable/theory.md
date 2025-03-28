# Hash table

build-in hash table is a dictionary type key, value

- Hash only have one way key -> value
- Is deterministic: We know the address all the time

## Collisions

Ocurres when we have another key-value pair in an address that already have a key-value pair.

How to avoid overwriting the old key-value pair? well we use a `separating chaining` we add each list inside a list.

Another way to work with separating chaining is using linked lists, so each key-value is going to be linked to the new key-pair that we are adding.
**\_Note: we should have an prime number of addresses in the list because it reduces the collisions**

`linear probing (open addressing)`
This technique consist in if a key-par was sent to an address that already have a key-pair, we are going to go down nad check if the next slot is empty, if yes we just added, if not, we continue going down until we found one

## Hash table Big O

- Hash method big o: same number of operations to calculate the hash `o(1)`
- set_item = `o(1)`
- get_item = find address and then find the key `o(1)`

The hash table is like a dictionary in python, and assuming that we are not going to have frecuent collides, this method is o(1)

## Interview question:

Sience a hash table is O(1) for insert and lookup it is always better that Binary Search Tree

Answer: No, Binary Search Tree are sorted which makes them better at searching for all values that fall within a range

# Sets

Sets are similar to dictionaries except that instead of having key/value pairs they only have keys.

Like dictioneries, they are implemented using a hash table

Sets can only contain unique elements

They are very useful to find distinct values in a collection and performing set operations such as union and intersection

They are defined by either using curly braces {} or the built-in set() function like this:

### Create a set using {}

my_set = {1, 2, 3, 4, 5}

### Create a set using set()

my_set = set([1, 2, 3, 4, 5])

Once a set is defined, you can perform various operations on it, such as adding or removing elements, finding the union, intersection, or difference of two sets, and checking if a given element is a member of a set.

Here are some examples of common set operations in Python:

### Add an element to a set

If the number 6 is already in the set it will not be added again.
my_set.add(6)

Update is used to add multiple elements to the set at once.
It takes an iterable object (e.g., list, tuple, set) as an
argument and adds all its elements to the set.
If any of the elements already exist in the set,
they are not added again.
my_set.update([3, 4, 5, 6])

### Removing an element from a set

my_set.remove(3)

### Union of two sets

other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)

### Intersection of two sets

intersection_set = my_set.intersection(other_set)

### Difference between two sets

difference_set = my_set.difference(other_set)

### Checking if an element is in a set

if "hello" in my_set:
print("Found hello in my_set")

You can learn more about sets by clicking here.

Now let's look at some common coding interview questions that use sets!
