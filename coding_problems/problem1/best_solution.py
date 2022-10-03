#Input: arr = [4, 5, 1, -3, 6], k = 11
#Output: true
#Explanation: 5 + 6 is equal to 11

#We will use the Hash table lookup insertion method
#The hash table will check if the element that I am serching for was already visited or not

def findPair(arr, k):
    visited = {}
    for element in arr:
        if visited.get(k-element): 
            return True
        else:
            visited[element] = True
    return False

                
#print(findPair([4, 5, 1, -3, 6],  11)) # true
#print(findPair([4, 5, 1, -3, 6],  -2)) # true
print(findPair([4, 5, 1, -3, 6],  8))  # false