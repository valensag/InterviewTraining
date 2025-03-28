def findPair(arr,k):
    seen = set()
    for element in arr:
        if k-element in seen:
            return True
        seen.add(element)
    return False

def findPair(arr,k):
    visited = {}
    for element in arr:
        if visited.get(k-element):
            return True
        else:
            visited[element] = True
    return False
    
    
    
arr = [8,2,9,5,10,1]
k = 12
print(findPair(arr,k))