def find_first_repeating_char(string: str):
    repeat_letters = {}
    for element in string:
        if repeat_letters.get(element):
            return element
        else:
            repeat_letters[element] = True
    return '/x00'
        
# def find_first_repeating_char(string: str):
#     repeat_letters = set()
#     for element in string.lower():
#         if element not in repeat_letters:
#             repeat_letters.add(element)
#         else:
#             return element
#     return '/O'


string = "inside code"
print(find_first_repeating_char(string))
string = "progRamming"
print(find_first_repeating_char(string))
string = "abcd"
print(find_first_repeating_char(string))
string = "abba"
print(find_first_repeating_char(string))