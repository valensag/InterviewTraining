def item_in_common(list1, list2):
    dict_common ={}
    for element in list1:
        dict_common[element] = True
    for element in list2:
        if element in dict_common:
            print(f"It's a common element: {element}")
            return True
    return False

def find_duplicates(nums):
    dict_nums = {}
    list_duplicated_nums = []
    for element in nums:
        if element in dict_nums and element not in list_duplicated_nums:
            list_duplicated_nums.append(element)
        dict_nums[element] = True
    return list_duplicated_nums

def first_non_repeating_char(string):
    dict_string = {}
    counter = 1
    for element in string:
        if element in dict_string:
            dict_string[element] += 1
        else:
            dict_string[element] = counter
    for key,value in dict_string.items():
        if value == 1:
            return key
    return None

def group_anagrams(list_strings):
    dict_anagrams = {}

    for word in list_strings:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in dict_anagrams:
            dict_anagrams[sorted_word] = [word]
        else:
            dict_anagrams[sorted_word].append(word)

    return list(dict_anagrams.values())

def two_sum(arr,k):
    dict_nums = {}
    for index,element in enumerate(arr):
        value = k - element
        if value in dict_nums:
            return sorted([index, dict_nums[value]])
        else:
            dict_nums[element] = index
    return []

def remove_duplicates(my_list):
    list_without_dups = set(my_list)
    return list(list_without_dups)

# def has_unique_chars(string):
#     if sorted(list(string)) == sorted(list(set(string))):
#         return True
#     else:
#         return False
    
def has_unique_chars(string):
    return len(set(string)) == len(string)

def find_pairs(arr1, arr2, target):
    set1=set(arr1)
    list_pairs = []
    for element in arr2:
        value = target - element
        if value in set1:
            list_pairs.append((value,element))
    return list_pairs
            
# def longest_consecutive_sequence(nums):
#     if not nums:
#         return 0
    
#     num_set = set(nums)
#     longest = 0
    
#     for num in num_set:
#         if num - 1 not in num_set:
#             current_num = num
#             current_length = 1
            
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_length += 1
            
#             longest = max(longest, current_length)
    
#     return longest

# def bubble_sort(my_list):
#     for i in range(len(my_list) - 1, 0, -1):
#         for j in range(i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    
#     return my_list

# def lambda_implementation(nums):
#     squared = map(lambda n: n**2,nums)
#     filtered = filter(lambda n: n%2==0,nums)
#     return list(filtered)

# def sorted_func(people):
#     sorted_people = sorted(people, key=lambda x: x[0])
#     return sorted_people
def decorator_hello(original_function):
    def wrapper(*args):
        print('This is your first day')
        return original_function(*args)
    return wrapper

@decorator_hello
def say_hello(name):
    print(f"Hello {name}")

result = say_hello('vale')


# nums = [1, 2, 3, 4, 5]
# print(lambda_implementation(nums))
    
# list1 = [1,3,5,1]
# list2 = [2,4,5]
# print(item_in_common(list1,list2))

# print ( find_duplicates([1, 2, 3, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 3]) )
# print ( find_duplicates([1, 1, 1, 1, 1]) )
# print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([]) )

# print( first_non_repeating_char('leetcode') )
# print( first_non_repeating_char('hello') )
# print( first_non_repeating_char('aabbcc') )

# print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

# print(two_sum([5, 1, 7, 2, 9, 3], 10))  
# print(two_sum([4, 2, 11, 7, 6, 3], 9))  
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
# print(two_sum([1, 3, 5, 7, 9], 10))  
# print ( two_sum([1, 2, 3, 4, 5], 10) )
# print ( two_sum([1, 2, 3, 4, 5], 7) )
# print ( two_sum([1, 2, 3, 4, 5], 3) )
# print ( two_sum([], 0) )   

# my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
# new_list = remove_duplicates(my_list)
# print(new_list)

# print(has_unique_chars('abcdefg')) 
# print(has_unique_chars('hello')) 
# print(has_unique_chars('')) 
# print(has_unique_chars('0123456789')) 
# print(has_unique_chars('abacadaeaf')) 

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]
# target = 7
# pairs = find_pairs(arr1, arr2, target)
# print (pairs)

# print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

# my_list = [64, 34, 25, 12, 22, 11, 90]
# sorted_list = bubble_sort(my_list)
# print("Sorted list:", sorted_list)

# people = [("John", 25), ("Jane", 30), ("Dave", 20)]
# print(sorted_func(people))