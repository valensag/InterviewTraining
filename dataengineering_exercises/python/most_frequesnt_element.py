def find_most_frequent_element(arr):
    dict_elements = {}
    for element in arr:
        if element in dict_elements.keys():
            dict_elements[element] += 1
        else:
            dict_elements[element] = 1
    return max(dict_elements, key=dict_elements.get)

arr = [1, 2, 3, 1, 1, 2]
print(find_most_frequent_element(arr))