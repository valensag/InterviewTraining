# Big O

It's a way to compare 2 codes with maths and check which is most efficient

- `Time complexity:` Not mesure in time. Is mesured in the number of operations that takes to do something
- `Space complexity:` how much memory takes the code to do something

### Concepts

- `alfa`: the best case scenario
- `teta`: the average case
- `omochron`: worst case

### Big O Diagram

![alt text](image-1.png)

### O(n)

Proportional the number of operations and n.

- Drop Constants: We could have (n+n) = 2n but no matter that, we can eliminate the constant and will be a problem type => o(n)

### O(n2)

(n \* n) => On2
Less efficient from time complexity stand point

- Drop Non Dominants: Here we have O(n2 + n) but the dominant is n2 so we drop the non dominant (n)
  ![alt text](image-2.png)

### O(1)

Just one operation, no matter anything else, it will be constant, we don't increase the number of operations, is the most efficient way to do operations

### O(log n)

We must have data sorted. for example a list of numbers
We take the list, cut it in the half, check in which half is the number that i'm searching, then we continue dividing until we find the number that we are searching for

log2 (8) = 3

Is very efficient for big lists

### O(nlogn)

Is the most efficient algorithm for sorting different kind of data

## Different Terms for inputs

o(a + b) or o(a \* b)

## Big O of Lists

Add or remove an element from a list in the last element is the best choice because we don't need to re order the index of the elements in the list, so is a o(1) but if we add or remove elements in the first part of the list for example, it's o(n)

## Wrap up

![alt text](image-3.png)
https://www.bigocheatsheet.com/
