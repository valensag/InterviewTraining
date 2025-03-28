# convertir un número romano en entero
def convert_roman_to_number(string:str)-> int:
    list_roman_numbers = list((string.upper()))
    print(list_roman_numbers)
    counter = 0
    prev = 0
    dict_roman_to_number = {"I":1, "V":5, "X":10}

    for value in reversed(list_roman_numbers):
        current = dict_roman_to_number[value]
        if current< dict_roman_to_number[prev]:
            counter -= current
        else:
          counter += current

    print(counter)


result = convert_roman_to_number('xx')