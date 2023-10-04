import os

def main(): # opens the MindFuck Script (currently only works with the test script).
    test_script_path = os.path.join(os.path.dirname(__file__), "Test.mfs")
    if not os.path.exists(test_script_path):
        raise FileNotFoundError(f"MindFuck Script: \"{test_script_path}\" doesn't exist")
    with open(test_script_path, "r", encoding="utf-8") as f:
        file_data = f.readlines()
    if len(file_data) == 0:
        return None
    run(file_data, test_script_path)
    exit()

def run(file_data : list, file_path : str): # interprets a script.
    array = [] # contains the values from 0 - 100.
    for num in range(0, 100):
        array.append(0)
    array_num = 0 # determines what index in the array the interpreter is pointing at.
    line_num = 0 # determines which line the interpreter should interpret.
    is_unicode_enabled = False # determines if MindFuck only uses Ascii characters or if it also uses Unicode characters.
    nested_while_loops = 0 # contains the amount nested while loops found inside a while loop.
    while_loop_data = [] # contains data about while loops.
    while line_num < len(file_data):
        line = file_data[line_num]
        char_num = 0 # determines which character the interpreter should interpret.
        while char_num < len(line):
            char = line[char_num]
            if char == "<": # moves to the left in the array.
                if array_num > 0:
                    array_num -= 1
            elif char == ">": # moves to the right in the array.
                if array_num < 100:
                    array_num += 1
            elif char == "+": # addition.
                if is_unicode_enabled == True:
                    if array[array_num] < 1023:
                        array[array_num] += 1
                else:
                    if array[array_num] < 127:
                        array[array_num] += 1
            elif char == "-": # subtraction.
                if array[array_num] > 0:
                    array[array_num] -= 1
            elif char == ".": # prints to console.
                if line[char_num + 1] == "!": # putting a "!" after a "." returns the decimal number instead of the ascii character.
                    print(array[array_num], end="")
                    char_num += 1
                elif line[char_num + 1] == "?": # putting a "?" after a "." goes to the next line in the console.
                    print()
                    char_num += 1
                elif line[char_num + 1] == "&": # putting a "&" after a "." returns the current index number.
                    print(array_num)
                    char_num += 1
                else: # prints the character in the Ascii or Unicode table.
                    print(chr(int(array[array_num])), end="")
            elif char == ",": # gets input from the console.
                in_input = input()
                if in_input == "":
                    array[array_num] = 0
                else:
                    array[array_num] = ord(in_input[0])
            elif char == "[": # begining of while loop.
                nested_while_loops += 1
                if array[array_num] == 0: # checks if the index in the array is 0. if true. it will not execute the while loop. if false. it will execute the while loop.
                    first_iteration = True # determines if it's the first iteration of the while loop on the next line.
                    current_nested_while_loops = nested_while_loops - 1 # contains the current amount of nested while loops before entering a new while loop.
                    while line_num < len(file_data): # loops through lines of the script until it finds the "]" of the while loop.
                        line = file_data[line_num]
                        if first_iteration == True:
                            char_num2 = char_num + 1
                            first_iteration = False
                        else:
                            char_num2 = 0
                        while char_num2 < len(line):
                            char = line[char_num2]
                            if char == "[":
                                nested_while_loops += 1
                            elif char == "]":
                                nested_while_loops -= 1
                            char_num2 += 1
                            continue
                        if nested_while_loops == current_nested_while_loops:
                            break
                        line_num += 1
                        continue
                else:
                    pass
            elif char == "]": # end of while loop.
                pass
            elif char == "#": # handles flags for MindFuck.
                if line[0:13] == "#unicode true": # enables Unicode.
                    is_unicode_enabled = True
                    char_num += 12
                elif line[0:14] == "#unicode false": # disables Unicode.
                    is_unicode_enabled = False
                    char_num += 13
            char_num += 1
            continue
        line_num += 1
        continue

if __name__ == "__main__":
    main()
