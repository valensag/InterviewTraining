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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        prep = self.head

        while(temp.next):
            prep = temp
            temp = temp.next
        self.tail = prep
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        prep = self.head
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(0)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
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

    def append_new(self, value):
        new_node = Node(value)
        temp = self.tail

        if temp is not None:
            temp.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_new(self):
        if self.length == 0:
            return None
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
            return current
        if current is not None:
            for _ in range(self.length):
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                    self.length -= 1
                    return current
                else:
                    prev = current
                    current = current.next
    
    def prepend_new(self,value):
        new_node = Node(value)
        if self.length >= 1:
            current = self.head
            self.head = new_node
            new_node.next = current
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_first_new(self):
        if self.length == 0:
            return None

        current = self.head
        self.head = current.next
        current.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current
    
    def get_new(self,index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for i in range(self.length-1):
            if index == i:
                return current
            current = current.next
    
    def set_new(self,index,value):
        if index < 0 or index >= self.length:
            return False
        current = self.get(index)
        current.value = value
        return True

    def insert_new(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        if index > 0:
            new_node = Node(value)
            prev = self.get(index-1)
            current = self.get(index)
            prev.next = new_node
            new_node.next = current
            self.length +=1
            return True

    def remove_new(self,index):
        if self.length == 0:
            return None
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        prev = self.get(index-1)
        current = self.get(index)
        prev.next = current.next
        current.next = None
        self.length -= 1
        return current

    def reverse_new(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.tail = self.head
        self.head = prev



      

# my_linked_list = LinkedList(4)

# my_linked_list.append(2)
# my_linked_list.append(6)
# my_linked_list.prepend(3)

# my_linked_list.pop()
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.pop_first()
# my_linked_list.print_list()

# val = my_linked_list.get(0)
# my_linked_list.set(0,9000)

# my_linked_list.insert(1,2000)
# my_linked_list.remove(0)
# my_linked_list.print_list()
# my_linked_list.reverse()
# my_linked_list.append_new(9)
# my_linked_list.append_new(4)
# my_linked_list.pop_new()
# my_linked_list.pop_new()
# print(my_linked_list.pop_new())
# print(my_linked_list.pop_new())
# print(my_linked_list.pop_new())
# print(my_linked_list.pop_new())
# my_linked_list.prepend_new(9)
# my_linked_list.prepend_new(10)
my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(9)
my_linked_list.append(7)

print('---before:')
my_linked_list.print_list()

print(f"Removed element: {my_linked_list.remove_new(0)}")

print('----after:')
my_linked_list.print_list()



