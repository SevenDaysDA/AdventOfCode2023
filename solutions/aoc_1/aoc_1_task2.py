
word_to_digit_table = {
    "one" : 1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9 } 




def reverse_str(right_str):
    return right_str[::-1]

def get_str_digit_index(str_line, reversed = False):
    '''
    
    '''
    lowest_index = 1000
    lowest_index_key = None

    for key in word_to_digit_table.keys():
        if reversed:
            index = str_line.find(reverse_str(key))
        else:
            index = str_line.find(key)

        if index != -1 and index < lowest_index:
            lowest_index = index
            lowest_index_key = word_to_digit_table.get(key)

    # In case list is empty
    if lowest_index == 1000:
        return False
    else:
        return lowest_index, lowest_index_key
    

# test_string = "eightwothree"
# test_1 = "12j3h1jhsevnjhj24"

# # print(get_str_digit_index(test_string))
# # print(get_str_digit_index(test_1))

# # index, key = (get_str_digit_index(reverse_str(test_string), True))

# index_key = get_str_digit_index(reverse_str(test_string), True)
# if index_key:
#     index,  key = index_key
#     print(index, key)
# else:
#     print("Dont do it")


def get_first_integer(string_list, reversed = False):

    no_integer = True
    n = 0

    return_value = 0

    index_key = get_str_digit_index(string_list, reversed)
    if index_key:
        index_str_digit,  key_str_digit = index_key
    else:
        index_str_digit = 1000

    while no_integer:
        if n == len(string_list)-1:
            no_integer = False

        value = string_list[n]
        if value.isnumeric() and n < index_str_digit:
            return value
        n += 1

    if index_key:
        return str(key_str_digit)
    
    return return_value

def number_in_line(line_str):
    first_d = get_first_integer(line_str)
    last_d = get_first_integer(line_str[::-1], True)           # Go through reversed list

    line_number = int(first_d + last_d)

    return line_number

def sum_file(file_path = 'solutions/aoc_1/input.txt' ):

    # Read file line by line:
    # Using readlines()
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    total_number = 0
    # Strips the newline character
    for line in Lines:
        total_number += number_in_line(line)
    
    print("Total number of document: ", total_number)

    return True

sum_file()

