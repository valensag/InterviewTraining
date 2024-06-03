#Input
arr = [4, 5, 1, -3, 6]
k = 8
def findPair(arr, k):
    visited = {}
    for element in arr:
        if visited.get(k-element):
            return True
        else:
            visited[element] = True
    return False

print(findPair(arr, k))

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""