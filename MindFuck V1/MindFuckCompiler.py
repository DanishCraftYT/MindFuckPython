import os
try:
    import py2exe
except(ModuleNotFoundError):
    raise ModuleNotFoundError("please install \"py2exe\" to compile mindfuck script")

mf_path = os.path.dirname(__file__)

"""
Development Started:
March 6, 2023 (3/6/2023)
"""

with open(os.path.join(mf_path, "Files.txt"), "r", encoding="utf-8") as f:
    files_data_newline = f.readlines()

files_data = []
for path in files_data_newline:
    files_data.append(path.rstrip("\n"))
    continue

class EmptyFileError(Exception):
    pass

def main(): # figures out what file to run.
    main_input = int(input("type line of path to file in the \"Files.txt\" file here: "))
    if files_data[main_input - 1][0:4] == "sol:":
        try:
            if files_data[main_input - 1].split(".")[1].lower() != "mfs":
                print(f"file: {os.path.join(mf_path, files_data[main_input - 1][4:])} doesn't end in \".mfs\"")
                input("hit enter to continue")
                main()
            if not os.path.exists(os.path.join(mf_path, files_data[main_input - 1][4:])):
                print(f"file: {os.path.join(mf_path, files_data[main_input - 1][4:])} doesn't exist")
                input("hit enter to continue")
                main()
            with open(os.path.join(mf_path, files_data[main_input - 1][4:]), "r", encoding="utf-8") as f:
                file_data = f.readlines()
            if not len(file_data) > 0: # checks if file is empty.
                raise EmptyFileError("the file your trying to compile is empty")
        except(IndexError):
            print(f"index: {main_input - 1} is more than {len(files_data)}. please type a lower number")
            input("hit enter to continue")
            main()
        else:
            use_icon(file_data, os.path.basename(files_data[main_input - 1]))
            exit()
    else:
        try:
            if files_data[main_input - 1].split(".")[1].lower() != "mfs":
                print(f"file: {os.path.join(mf_path, files_data[main_input - 1][4:])} doesn't end in \".mfs\"")
                input("hit enter to continue")
                main()
            if not os.path.exists(files_data[main_input - 1]): # checks if the file exists.
                print(f"file: {files_data[main_input - 1]} doesn't exist")
                input("hit enter to continue")
                main()
            with open(files_data[main_input - 1], "r", encoding="utf-8") as f:
                file_data = f.readlines()
            if not len(file_data) > 0: # checks if file is empty.
                raise EmptyFileError("the file your trying to compile is empty")
        except(IndexError):
            print(f"index: {main_input - 1} is more than {len(files_data)}. please type a lower number")
            input("hit enter to continue")
            main()
        else:
            use_icon(file_data, os.path.basename(files_data[main_input - 1]))
            exit()

def use_icon(file_data, name_of_script):
    icon_path = input("use a icon for the .exe file? type: <path_to_icon_file> or No here: ").lower()
    if icon_path == "no":
        compiler(file_data, name_of_script)
    elif icon_path != "no":
        if not os.path.exists(icon_path):
            raise FileNotFoundError(f"file: \"{icon_path}\" not found")
        compiler(file_data, name_of_script, icon_path)

def compiler(file_data, name_of_script, icon_path=None):
    name_of_script = name_of_script.rstrip(".mfs")
    with open(os.path.join(mf_path, f"{name_of_script}.py"), "w", encoding="utf-8") as f:
        f.write("file_data = [")
        for i, line in enumerate(file_data):
            line = line.rstrip("\n")
            if i == len(file_data) - 1:
                f.write(f"\"{line}\"]\n\n")
                break
            else:
                f.write(f"\"{line}\", ")
                continue
        # writting code for the interpreter in .py file:
        f.write("""class FunctionError(Exception):
    pass

class LoopError(Exception):
    pass

def run(file_data): # runs the code in the file.
    if not len(file_data) > 0: # checks if file is empty.
        exit()
    array = []
    for num in range(0, 100):
        array.append(0)
        continue
    array_num = 0 # current number in array.
    line_num = 0 # current line in file.
    # If Statement Varibles:
    current_if_operator = "" # the if operator.
    is_in_if_statement_defined = False # determines if the if statement has reached "}" the the if statement is false.
    is_finding_second_index = False # if the if statement is finding the second index.
    find_if_statement_operator = False
    current_index_num_2 = None # is set to the current index number. used for if statements.
    # Function Varibles:
    is_in_function_defined = False # determines if the function has reached ")" right after it has been defined.
    func_start = None # start of function.
    current_line = None # the current line when calling a function.
    current_char = None # the current char when calling a function.
    # While Loop Varibles:
    current_index_num = None # is set to the current index number. used in if statements and while loops.
    # Hashtag Varibles:
    is_unicode_enabled = False
    while line_num <= len(file_data):
        line = file_data[line_num]
        char_num = 0 # current character in line.
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
            if is_in_if_statement_defined == True:
                if char == "}":
                    char_num += 1
                    is_in_if_statement_defined = False
                    break
                char_num += 1
                if char_num == len(line):
                    break
                continue
            if find_if_statement_operator == True:
                current_if_operator += char
                if len(current_if_operator) > 2:
                    current_if_operator = current_if_operator[0:2]
            elif char == "<":
                if array_num > 0:
                    array_num -= 1
            elif char == ">":
                if array_num < 100:
                    array_num += 1
            if char == "+":
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
                    array[array_num] = ord(in_input[0])
            elif char == "\\\\": # beginning of if statement.
                is_finding_second_index = True
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
                if is_finding_second_index == True:
                    current_index_num = array[array_num]
                else:
                    current_index_num = array[array_num]
                    current_char_while = char_num + 1
                    current_line_while = line_num
            elif char == "]": # end of while loop.
                if is_finding_second_index == True:
                    current_index_num_2 = array[array_num]
                    find_if_statement_operator = True
                    is_finding_second_index = False
                else:
                    if current_index_num == None:
                        raise LoopError("no while loop is defined")
                    current_index_num -= 1
                    if current_index_num == 0:
                        char_num += 1
                        continue
                    char_num = current_char_while + 1
                    line_num = current_line_while
            elif char == "{":
                find_if_statement_operator = False
                if current_if_operator[1] != "=":
                    current_if_operator = current_if_operator[0]
                if current_if_operator == "<":
                    if current_index_num < current_index_num_2:
                        char_num += 1
                    else:
                        is_in_if_statement_defined = True
                elif current_if_operator == ">":
                    if current_index_num > current_index_num_2:
                        char_num += 1
                    else:
                        is_in_if_statement_defined = True
                elif current_if_operator == "==":
                    if current_index_num == current_index_num_2:
                        char_num += 1
                    else:
                        is_in_function_defined = True
                elif current_if_operator == "!=":
                    if current_index_num != current_index_num_2:
                        char_num += 1
                    else:
                        is_in_if_statement_defined = True
                elif current_if_operator == "<=":
                    if current_index_num <= current_index_num_2:
                        char_num += 1
                    else:
                        is_in_if_statement_defined = True
                elif current_if_operator == ">=":
                    if current_index_num >= current_index_num_2:
                        char_num += 1
                    else:
                        is_in_if_statement_defined = True
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
    run(file_data)""")
    print("creating .exe file")
    if icon_path == None:
        py2exe.freeze(
            console = [{"script": f"{name_of_script}.py"}],
            options = {"py2exe": {"bundle_options": 0, "dist_dir": os.path.join(mf_path, f"dist")}},
            zipfile = None)
    elif icon_path != None:
        py2exe.freeze(
            console = [{"script": f"{name_of_script}.py", "icon_resources": [(0, icon_path)]}],
            options = {"py2exe": {"bundle_options": 0, "dist_dir": os.path.join(mf_path, f"dist")}},
            zipfile = None)
    print("finished creating .exe file")
    keep_python_script(name_of_script)

def keep_python_script(name_of_script):
    keep_py_script = input(f"delete \"{name_of_script}.py\"? type Yes or No here: ").lower()
    if keep_py_script == "yes":
        os.remove(f"{name_of_script}.py")
        input("hit enter to exit script")
        exit()
    elif keep_py_script == "no":
        input("hit enter to exit script")
        exit()
    else:
        print("please type: Yes or No")
        input("hit enter to continue")
        keep_python_script(name_of_script)

if __name__ == "__main__":
    main()
