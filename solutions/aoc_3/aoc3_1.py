

file_path = 'solutions/aoc_3/test_case1.txt' 
# file_path = 'solutions/aoc_3/input_aoc3_1.txt' 
# file_path = 'solutions/aoc_3/input_instruction.txt' 


instruction_array = []

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            instruction_array.append(line.strip())  # Use strip() to remove leading/trailing whitespace, including '\n'

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print("An error occurred:", e)



id_map = []

for instruct_id, instruct_line in enumerate(instruction_array):

    still_number = False
    number_acc = ""
    for line_id, char in enumerate(instruct_line):
        
        if char.isdigit():
            if not still_number:
                begin_id = line_id
            number_acc += char
            still_number = True
        else:
            # Either symbol or dot
            if still_number or line_id == len(instruct_line)-1:
                end_id = line_id
                id_map.append((instruct_id, [begin_id, end_id], number_acc))     # (line_id, [range_ids], value)
                number_acc = ""
                still_number = False

# id_map - contains all numbers
# print(id_map)



def check_relevance(map_entry, instruct_id, line_id):
    map_row, map_row_range, _ = map_entry
    if instruct_id >= map_row -1  and instruct_id <= map_row +1 :
        if line_id >= map_row_range[0] -1 and line_id <= map_row_range[1]+1:
            return True
    return False

result_value = 0
for instruct_id, instruct_line in enumerate(instruction_array):
    print()
    for line_id, char in enumerate(instruct_line):
        # print(char)
        # Here we find a symbol:
        if not char.isdigit() and not char == "." or char == "*":
            print(char)
            # print(instruct_id, line_id)
            # Iterate through all numbers:
            for num in id_map:
                print(num)
                # if char == "#":
                #     print(num)
                if check_relevance(num, instruct_id, line_id):
                    # print(char)
                    value = int(num[2])
                    print(value)
                    result_value += value

print(result_value)


to_low = 552835
not_right = 567632
to_high = 604596

# 556367
print(instruction_array)