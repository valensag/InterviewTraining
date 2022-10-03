def remove_duplicated(arr):
    seen = set()
    duplicated = [i for i in arr if i in seen or seen.add(i)]
    return set(duplicated)
            
#print(remove_duplicated([1, 4, 2, 2, 5, 2]))
print(remove_duplicated([4, 2, 1, 3, 1]))