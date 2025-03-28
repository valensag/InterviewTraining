def LongestWord(sen):
    words_dict = {}
    words_list = sen.split()
    for element in words_list:
        clean_element = ''.join([letter for letter in element if letter.isalpha()])
        words_dict[clean_element] = len(clean_element)
    return max(words_dict, key=words_dict.get)

# keep this function call here 
print(LongestWord('fun&!! time'))