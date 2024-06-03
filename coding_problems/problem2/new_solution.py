
string = "insde co"
def firstRepeatingCharacter(string): 
    char_dict = {}
    for item in list(string):
        if char_dict.get(item):
            return item
        else:
            char_dict[item] = True
    return '\x00'
   

print(firstRepeatingCharacter(string))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""