#1
import os

def list_items(path):
    #directories
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    
    #files
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    #directories and files
    all_items = os.listdir(path)
    
    print(dirs)
    
    print(files)
    
    print(all_items)

path = input("Enter the path: ")
list_items(path)

#2
import os

def check_access(path):
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = input("Enter path to check access: ")
check_access(path)

#3
import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("The path exists ")
    print("Directory part:", os.path.dirname(path))
    print("File name part:", os.path.basename(path))
else:
    print("The path does not exist")

#4
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

file_path = input("Enter file path: ")
print("Number of lines:", count_lines(file_path))

#5
def write_list_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(str(item) + '\n')

data = ["Hello", "World", "Python"]
file_path = input("Enter file path: ")
write_list_to_file(file_path, data)

#6
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is {letter}.txt")

#7
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src:
        with open(destination, 'w', encoding='utf-8') as dst:
            dst.write(src.read())
    print("File copied successfully.")

source = input("Enter source file path: ")
destination = input("Enter destination file path: ")
copy_file(source, destination)

#8
import os
path = input("Enter file path to delete: ")

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("No write permission. Cannot delete the file.")
    else:
        print("File does not exist.")

delete_file(path)
