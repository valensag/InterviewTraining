# LinkedList

- linked list **don't have index** as the normal lists
- is a contiguous place in memory but in linkedlist all of the nodes are going to be spread all ovver the place

![](image.png)

# Big O

- Append an element at the end of a linked list, in the tail have a complexity of O(1) because the number of operations is just 1
  ![alt text](image-1.png)

But what happend if we need to remove the item? it's complicated because we need to find another pointer to add the tail, and the next one is the one that is in the 23 so we have to iterate throw all the elements to find it O(n).

It's different if we need to remove an element from the beginning, because we just have to use one operation O(n)

![alt text](image-2.png)

## LL Under the hood

What is a Node?
its a dictionary with a value and a pointer

```py
dict1 = {"value": 4,
         "next": none}
```

How do we connect each node? well the "next" value becomes the next node dictionary

```py
dict1 = {"value": 11,
         "next": {"value": 3,
                "next": {"value": 23,
                        "next": {"value": 7,
                                "next": {"value": 4,
                                        "next": none
                                        }
                                }
                        }
                }
        }
print(head['next']['next']['value'])
------------------------------------------------
23
```

So if we have a linked list, the way to access the information is very similar, should be like the following:

` print(my_linked_list.head.next.next.value)`

# Constructor

Here we created the class Node that will just create nodes, we use this clas in the constructor of the linked list

```py
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
---------------------------------
4
```

# Print List

To look all of the elements in a link list

```py
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)


my_linked_list.append(2)

my_linked_list.print_list()
----------------------
4  2

```

# Pop

my solution:

```py
    def pop(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value

        #traverse to find second last node
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value
```

# Prepend

my solution

```py
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            pre_node = self.head
            self.head = new_node
            self.head.next = pre_node
        self.length += 1
```

# Pop first

my solution

```py
    def pop_first(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        temp = self.head
        prep = self.head
        while(temp.next):
            temp = temp.next
            self.head = temp
            self.length -= 1
            return True
```

# Get

```py
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value


```

# Set

```py
    def set(self, index, value):
        temp = self.get(0)
        if temp:
            temp.value = value
            return True
        return False

```

# Insert

```py
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None

        pre = self.get(index-1)
        post = self.get(index)

        if pre is not None and post is not None:
            new_node = Node(value)
            pre.next = new_node
            new_node.next = post
        return True
```

# Remove

```py
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        pre = self.get(index-1)
        temp = self.get(index)

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
```

# Reverse

```py
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.tail = self.head
        self.head = prev
```
