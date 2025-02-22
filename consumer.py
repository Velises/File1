import os
import shutil
from dataclasses import dataclass
import time

@dataclass
class Point():
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


_path = r"Download\\"
_error_path = "Error\\"

def make_dir():
    dir = os.path.dirname(_error_path)
    os.makedirs(dir, exist_ok=True)

def walk_path():
    listDir = os.walk(_path)
    for (root, dirs, files) in listDir:
        for file in files:
            if '.json' in file:
                print(file)
            else:
                move_to_error(file)

def move_to_error(file: str):
    shutil.copy2(f"{_path}{file}", f"{_error_path}{file}")
    os.remove(f"{_path}{file}")

def main():
    print("START")
    make_dir()
    while True:
        walk_path()
        time.sleep(10)

if __name__ == "__main__":
    main()