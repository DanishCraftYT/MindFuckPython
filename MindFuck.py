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

def main(): # figures out what file to run.
    main_input = int(input("type line of path to file in the \"Files.txt\" file here: "))
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
    while line_num <= len(file_data):
        line = file_data[line_num]
        char_num = 0 # current character in line.
        while char_num <= len(line):
            char = line[char_num]
            if char == "<":
                array_num -= 1
            elif char == ">":
                array_num += 1
            elif char == "+":
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
                if array[array_num] == array[array_num] * 2 > 127:
                    array[array_num] = 127
                else:
                    array[array_num] = array[array_num] * 2
            elif char == "/":
                if array[array_num] == array[array_num] / 2 < 0:
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
                    else:
                        print(chr(int(array[array_num])), end="")
                except(IndexError):
                    print(chr(int(array[array_num])), end="")
            elif char == ",":
                array[array_num] = ord(input()[0])
            elif char == "/": # beginning of if statement.
                pass
            elif char == "\\": # end of if statement.
                pass
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
