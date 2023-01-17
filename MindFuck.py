import os

mf_path = os.path.dirname(__file__)

with open(os.path.join(mf_path, "Files.txt"), "r", encoding="utf-8") as f:
    files_data = f.readlines()

def main(): # figures out what file to run.
    main_input = input("type line of path to file in the \"Files.txt\" file here: ")
    try:
        if not os.path.exists(files_data[main_input - 1]):
            print(f"file: {files_data[main_input - 1]} doesn't exist")
            input("hit enter to continue")
            main()
        with open(files_data[main_input - 1], "r", encoding="utf-8") as f:
            file_data = f.readlines()
        run(file_data)
    except(IndexError):
        print(f"index: {main_input - 1} is more than {len(files_data)}. please type a lower number")
        input("hit enter to continue")
        main()

def run(file_data): # runs the code in the file.
    line_num = 0
    while line_num <= len(file_data):
        line = file_data[line_num]
        char_num = 0
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
