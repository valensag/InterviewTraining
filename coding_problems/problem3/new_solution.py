# Parameters:
#  arr: List[int]
# return type: List[int]

arr = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]

def removeDuplicates(arr):
    return list(set(arr))

print(removeDuplicates(arr))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

