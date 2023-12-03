
file_path = 'solutions/aoc_3/input_instruction.txt' 

instruction_array = []

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
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
        
        if char.isnumeric():
            if not still_number:
                begin_id = line_id
            number_acc += char
            still_number = True
        else:
            # Either symbol or dot
            if still_number:
                end_id = line_id
                id_map.append((instruct_id, [begin_id, end_id], number_acc))     # (line_id, [range_ids], value)
                number_acc = ""
                
            still_number = False

# id_map - contains all numbers
print(id_map)