import os

mf_path = os.path.dirname(__file__)

"""
Development Started:
January 17, 2023 (1/172023)
"""

with open(os.path.join(mf_path, "Files.txt"), "r", encoding="utf-8") as f:
    files_data_newline = f.readlines()

files_data = []
for path in files_data_newline:
    files_data.append(path.rstrip("\n"))
    continue

class FunctionError(Exception):
    pass

class LoopError(Exception):
    pass

def main(): # figures out what file to run.
    main_input = int(input("type line of path to file in the \"Files.txt\" file here: "))
    if files_data[main_input - 1][0:4] == "sol:":
        try:
            if not os.path.exists(os.path.join(mf_path, files_data[main_input - 1][4:])):
                print(f"file: {os.path.join(mf_path, files_data[main_input - 1][4:])}")
                input("hit enter to continue")
                main()
            with open(os.path.join(mf_path, files_data[main_input - 1][4:]), "r", encoding="utf-8") as f:
                file_data = f.readlines()
            if not len(file_data) > 0: # checks if file is empty.
                exit()
        except(IndexError):
            print(f"index: {main_input - 1} is more than {len(files_data)}. please type a lower number")
            input("hit enter to continue")
            main()
        else:
            run(file_data)
            exit()
    else:
        try:
            if not os.path.exists(files_data[main_input - 1]): # checks if the file exists.
                print(f"file: {files_data[main_input - 1]} doesn't exist")
                input("hit enter to continue")
                main()
            with open(files_data[main_input - 1], "r", encoding="utf-8") as f:
                file_data = f.readlines()
            if not len(file_data) > 0: # checks if file is empty.
                exit()
        except(IndexError):
            print(f"index: {main_input - 1} is more than {len(files_data)}. please type a lower number")
            input("hit enter to continue")
            main()
        else:
            run(file_data)
            exit()

def run(file_data): # runs the code in the file.
    array = []
    for num in range(0, 100):
        array.append(0)
        continue
    array_num = 0 # current number in array.
    line_num = 0 # current line in file.
    func_start = None
    current_line = None
    current_char = None
    current_index_num = None
    is_in_function_defined = False # determines if the function has reached ")" right after it has been defined.
    is_unicode_enabled = False
    while line_num <= len(file_data):
        line = file_data[line_num]
        char_num = 0 # current character in line.¨
        while char_num <= len(line):
            try: # used for after functions has been defined and for when while loops are done running.
                char = line[char_num]
            except(IndexError):
                break
            if is_in_function_defined == True:
                if char == ")":
                    char_num += 1
                    is_in_function_defined = False
                    break
                char_num += 1
                if char_num == len(line):
                    break
                continue
            if char == "<":
                array_num -= 1
            elif char == ">":
                array_num += 1
            elif char == "+":
                if is_unicode_enabled == True:
                    if array[array_num] + 1 > 1023:
                        array[array_num] = 1023
                    else:
                        array[array_num] += 1
                elif is_unicode_enabled == False:
                    if array[array_num] + 1 > 127:
                        array[array_num] = 127
                    else:
                        array[array_num] += 1
            elif char == "-":
                if array[array_num] - 1 < 0:
                    array[array_num] = 0
                else:
                    array[array_num] -= 1
            elif char == "*":
                if is_unicode_enabled == True:
                    if array[array_num] * 2 > 1023:
                        array[array_num] = 1023
                    else:
                        array[array_num] = array[array_num] * 2
                elif is_unicode_enabled == False:
                    if array[array_num] * 2 > 127:
                        array[array_num] = 127
                    else:
                        array[array_num] = array[array_num] * 2
            elif char == "/":
                if array[array_num] / 2 < 0:
                    array[array_num] = 0
                else:
                    array[array_num] = array[array_num] / 2
            elif char == ".":
                try:
                    if line[char_num + 1] == "!": # putting a "!" after a "." returns the decimal number instead of the ascii character.
                        print(array[array_num], end="")
                        char_num += 1
                    elif line[char_num + 1] == "?": # putting a "?" after a "." goes to the next line in the console.
                        print("")
                        char_num += 1
                    elif line[char_num + 1] == "&": # putting a "&" after a "." returns the current index number.
                        print(array_num)
                        char_num += 1
                    else:
                        print(chr(int(array[array_num])), end="")
                except(IndexError):
                    print(chr(int(array[array_num])), end="")
            elif char == ",":
                in_input = input()
                if in_input == "":
                    array[array_num] = 0
                else:
                    array[array_num] = ord(input()[0])
            elif char == "/": # beginning of if statement.
                pass
            elif char == "\\": # end of if statement.
                pass
            elif char == "(": # start of function.
                func_start = line_num
                func_start_char = char_num + 1
                is_in_function_defined = True
                break
            elif char == ":": # calls function.
                current_line = line_num
                current_char = char_num + 1
                if func_start == None or current_line == None or current_char == None:
                    raise FunctionError("no function is defined")
                line_num = func_start
                char_num = func_start_char
            elif char == ")": # end of function.
                line_num = current_line
                char_num = current_char
            elif char == "[": # start of while loop.
                current_index_num = array[array_num]
                current_char_while = char_num + 1
                current_line_while = line_num
            elif char == "]": # end of while loop.
                if current_index_num == None:
                    raise LoopError("no while loop is defined")
                current_index_num -= 1
                if current_index_num == 0:
                    char_num += 1
                    continue
                char_num = current_char_while + 1
                line_num = current_line_while
            elif char == "#":
                if line[0:13] == "#unicode true":
                    is_unicode_enabled = True
                    char_num += 13
                    continue
                elif line[0:14] == "#unicode false":
                    is_unicode_enabled = False
                    char_num += 14
                    continue
            char_num += 1
            if char_num == len(line):
                break
            continue
        line_num += 1
        if line_num == len(file_data):
            break
        continue

if __name__ == "__main__":
    main()
