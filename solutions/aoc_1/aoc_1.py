

def get_first_integer(string_list):

    no_integer = True
    n = 0

    return_value = 0

    while no_integer:
        if n == len(string_list):
            no_integer = True
        value = string_list[n]
        if value.isnumeric():
            return value
        n += 1
    return return_value

def number_in_line(line_str):
    first_d = get_first_integer(line_str)
    last_d = get_first_integer(line_str[::-1])           # Go through reversed list

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





