#Input: arr = [4, 5, 1, -3, 6], k = 11
#Output: true
#Explanation: 5 + 6 is equal to 11


#FIRST SOLUTION
from ast import Try
from pickle import FALSE


def findPair(arr, k):
    #x = lambda a : a + 10
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == k:
                return True
            
    return False
                
print(findPair([4, 5, 1, -3, 6],  11)) # true
print(findPair([4, 5, 1, -3, 6],  -2)) # true
print(findPair([4, 5, 1, -3, 6],  8))  # false



