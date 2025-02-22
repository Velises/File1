


import os 
from dataclasses import dataclass
import random 
import json
from datetime import datetime
import time
import schedule

@dataclass
class Point():
    x: int
    y: int

    def __init__(self):
        self.x = random.randint(1, 999)
        self.y = random.randint(1, 999)




_i = 2
_time = 5

def write_file(text: str, num: int):
    now = datetime.now()

    dt_string = now.strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"{dt_string}_point_{num}.json"
    path = fr"Download\{file_name}"
    dir = os.path.dirname(path)
    os.makedirs(dir, exist_ok=True)
    with open(path, "a") as f:
        f.writelines(text )



def cycle():
    i = 0
    while i <= _i:
        i += 1
        point = Point()
        text = json.dumps(point.__dict__)

        write_file(text, i)

def main():
    print("START")
    schedule.every(_time).seconds.do(cycle)
    while True:
        schedule.run_pending()
        time.sleep(1)

cycle()
print("OK")


if __name__ == "__main__":
    main()

# with open('exapmle.txt', 'x') as f:
    # открытие файла и работа с ним
#    f.writelines("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
