def remove_duplicated(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]

#print(remove_duplicated([1, 4, 2, 2, 5, 2]))
print(remove_duplicated([4, 2, 1, 3, 1]))
        