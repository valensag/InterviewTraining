
#Input: arr = [4, 5, 1, -3, 6], k = 11
#Output: true
#Explanation: 5 + 6 is equal to 11

#We will use the two pointers method

def findPair(arr, k):
    arr.sort()
    left = 0
    right = len(arr) -1
    while left < right:
        if arr[left] + arr[right] == k:
            return True
        elif arr[left] + arr[right] < k:
            left += 1
        else:
            right -= 1
    return False

                
print(findPair([4, 5, 1, -3, 6],  11)) # true
print(findPair([4, 5, 1, -3, 6],  -2)) # true
print(findPair([4, 5, 1, -3, 6],  8))  # false