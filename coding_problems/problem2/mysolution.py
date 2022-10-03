# Given a string str, create a function that returns the first repeating character.
# If such character doesn't exist, return the null character '\0'.
# Example 1:
# Input: str = "inside code"
# Output: 'i'

# Example 2:
# Input: str = "programming"
# Output: 'r'

# Example 3:
# Input: str = "abcd"
# Output: '\0'

# Example 4:
# Input: str = "abba"
# Output: 'b'


def find_first_repeat(str):
    visited = {}
    for element in list(str):
        if visited.get(element):
            return(element)
        else:
            visited[element] = True
    return '\O'

#print(find_first_repeat("inside code"))
#print(find_first_repeat("programming"))
#print(find_first_repeat("abcd"))
print(find_first_repeat("abba"))