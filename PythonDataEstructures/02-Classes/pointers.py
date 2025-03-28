# num1 = 1
# num2 = num1

# print('Before')
# print(f"num1: {num1} id: {id(num1)}")
# print(f"num2: {num2} id: {id(num2)}")

# num2 = 12
# print('After')
# print(f"num1: {num1} id: {id(num1)}")
# print(f"num2: {num2} id: {id(num2)}")


dict1 = {'value':2}
dict2 = dict1

print('Before')
print(f"dict1: {dict1} id: {id(dict1)}")
print(f"dict2: {dict2} id: {id(dict2)}")

dict2['value'] = 40
print('After')
print(f"dict1: {dict1} id: {id(dict1)}")
print(f"dict2: {dict2} id: {id(dict2)}")