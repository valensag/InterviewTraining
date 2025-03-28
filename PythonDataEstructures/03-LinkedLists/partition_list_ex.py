class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
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
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self,x):
        if self.length == 0:
            return None
        dummy1 = LinkedList(None)
        dummy2 = LinkedList(None)
        dummy1.make_empty()
        dummy2.make_empty()
        current = self.head
        while current:
            if current.value < x:
                dummy1.append(current.value)
            else:
                dummy2.append(current.value)
            current = current.next
        
        if dummy1.tail:
            dummy1.tail.next = dummy2.head
        else:
            dummy1.head = dummy2.head

        dummy1.tail = dummy2.tail
        dummy1.length += dummy2.length
        return dummy1
        
        
            

my_linked_list = LinkedList(3)
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(2)
my_linked_list.append(5)
# my_linked_list.append(7)
x = 3
dummy1 = my_linked_list.partition_list(x)
dummy1.print_list()


