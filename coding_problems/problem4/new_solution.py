# Parameters:
#  arr: List[int]
# return type: int


arr = [4, 2, 1, 3, 1]

def findDuplicate(arr):
    visited = {}
    arr.sort()
    for item in arr:
        if visited.get(item):
            return item
        else:
            visited[item] = True
    return False

print(findDuplicate(arr))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""