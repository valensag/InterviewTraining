#Input
arr = [4, 5, 1, -3, 6]
k = 8
def findPair(arr, k):
    for key,v in enumerate(arr):
        result = k - v
        if result in arr[key+1:]:
            return True
    return False

findPair(arr, k)

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


