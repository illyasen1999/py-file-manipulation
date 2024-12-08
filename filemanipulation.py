import os
import pathlib as pt
import shutil
import datetime as dt

# TODO: directory is created but cant proceed with file creation
def create_path(filepath: str):
    f_path = os.mkdir(filepath)
    if os.path.exists(f_path):
        f_name = input("Enter file name: ")
        created_file = create_file(f_name)
        with os.open(created_file, 'w') as f:
            print("File created!")
            text = input("Enter text: ")
            f.write(text)
    else:
        pass

def create_file(filename: str):
    file = f"{filename}.txt"
    try:
        with open(file, "x") as f:
            return f
    except FileExistsError:
        print(f"{filename}.txt already exists")

def main():
    path_name = input("Enter path name: ")
    create_path(path_name)

if __name__ == "__main__":
    main()