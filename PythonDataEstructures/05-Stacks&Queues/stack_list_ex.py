
class Stack:
    def __init__(self):
        self.stack_list = []
        self.length = 0
    
    def print_elements(self):
        for i in self.stack_list:
            print(i)
    
    def push(self,value):
        self.stack_list.append(value)
        self.length += 1

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        else:
            self.stack_list.pop()
            self.length -= 1  

def is_balanced_parentheses(string):
    my_stack = Stack().stack_list
    for element in string:
        if element == '(':
            my_stack.append(element)
        elif element == ')':
            if len(my_stack) == 0:
                return False
            my_stack.pop()
    if len(my_stack) > 0:
        return False
    else:
        return True
    
def reverse_string(string):
    return string[::-1]

# print(reverse_string('hello'))
# print(is_balanced_parentheses( '(()'))
# my_stack.pop()
# my_stack.print_elements()
stack = Stack()


    