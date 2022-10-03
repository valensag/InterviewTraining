# We will use linked list with fast and slow pointer technique
def remove_duplicated(arr):
    tortoise = arr[0]
    hare = arr[arr[0]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise

#print(remove_duplicated([1, 4, 2, 2, 5, 2]))
print(remove_duplicated([5,2,4,2,1,6,3]))