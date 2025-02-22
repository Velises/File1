import os
import shutil
from dataclasses import dataclass
import time
import json


@dataclass
class Point():
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


_path = "Download\\"
_error_path = "Error\\"
_loaded_path = "Loaded\\"


def make_dir(path):
    dir = os.path.dirname(path)
    os.makedirs(dir, exist_ok=True)

def dedeserialize_point(file_name: str) -> Point | None:
    try:
        with open(f"{_path}{file_name}", "r") as f:
            text = f.readline()
        p = json.loads(text)
        result = Point(p["x"], p["y"])
        return result
    except Exception as e:
        print("The error is: ", e)
        return None

def walk_path():
    listDir = os.walk(_path)
    for (root, dirs, files) in listDir:
        for file_name in files:
            if '.json' in file_name:
                point = dedeserialize_point(file_name)
                if point == None:
                    move_to_error(file_name)
                else:
                    move_to_loaded(file_name)
                    print_point(point)

            else:
                move_to_error(file_name)
                print_point(point)


def print_point(point: Point):
    print(f"Point: X = {point.x}; Y = {point.y}")

def move_to_error(file: str):
    shutil.copy2(f"{_path}{file}", f"{_error_path}{file}")
    os.remove(f"{_path}{file}")


def move_to_loaded(file: str):
    shutil.copy2(f"{_path}{file}", f"{_loaded_path}{file}")
    os.remove(f"{_path}{file}")

def main():
    print("START")
    make_dir(_path)
    make_dir(_error_path)
    make_dir(_loaded_path)
    while True:
        walk_path()
        time.sleep(10)

if __name__ == "__main__":
    main()