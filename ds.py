import os
from time import strftime, gmtime

root_path = 'C:\\Users\\Pavel_Goncharenko\\Documents\\Lightshot'

st = len(root_path) + 1 # путь вырезаем отсюда

def print_dir(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                print_dir(entry.path)
    with os.scandir(path) as it:
        for entry in it:
            stat = entry.stat()
            created = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(stat.st_ctime))
            size = round(stat.st_size / 1024, 2)
            if not entry.name.startswith('.') and entry.is_file():
                print('{0}, {1}'.format(entry.path[st:], size))

print_dir(root_path)
