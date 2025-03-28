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
  
def find_kth_from_end(self,k):
    slow = fast = self.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow


    




        
            


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 10
result = find_kth_from_end(my_linked_list, k)

print(result)  # Output: 4
