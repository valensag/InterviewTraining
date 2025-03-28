class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        counter = 0
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            counter += 1
            if fast is None:
                return slow
        return slow

    
            

    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print(my_linked_list.find_middle_node().value)