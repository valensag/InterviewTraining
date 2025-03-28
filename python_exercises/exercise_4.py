def find_duplicate(arr):
    visited = {}
    for item in arr:
        if visited.get(item):
            return item
        else:
            visited[item] = True
    return False

arr = [4, 2, 1, 3, 1]
print(find_duplicate(arr))