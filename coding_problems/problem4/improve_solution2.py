def remove_duplicated(arr):
    visited = {}
    for i in arr:
        if visited.get(i):
            return(i)
        else:
            visited[i] = True

print(remove_duplicated([1, 4, 2, 2, 5, 2]))
#print(remove_duplicated([4, 2, 1, 3, 1]))
        