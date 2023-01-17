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
        if not os.path.getsize(files_data[main_input - 1]) > 0: # checks if file is empty.
            exit()
        with open(files_data[main_input - 1], "r", encoding="utf-8") as f:
            file_data = f.readlines()
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
    print(len(array))
    line_num = 0 # current line in file.
    while line_num <= len(file_data):
        line = file_data[line_num]
        char_num = 0 # current character in line.
        while char_num <= len(line[line_num]):
            char = line[char_num]
            char_num += 1
            if char_num == len(line[line_num]):
                break
            continue
        line_num += 1
        if line_num == len(file_data):
            break
        continue

if __name__ == "__main__":
    main()
