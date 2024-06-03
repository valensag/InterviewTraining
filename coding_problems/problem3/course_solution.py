arr = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
def removeDuplicates(arr):
    visited = {}
    for element in arr:
        visited[element] = True
    return list(visited.keys())