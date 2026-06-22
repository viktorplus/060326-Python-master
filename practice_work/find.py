#!/usr/sbin/python

""" 03 Файлы с заданным расширением

Напишите программу, которая:
- принимает путь к директории и расширение файлов через аргументы командной строки.
- ищет файлы с указанным расширением в указанной директории.
- выводит список найденных файлов

Пример запуска
python script.py /home/user/projects .py
Пример вывода
Найденные файлы в директории '/home/user/projects': script.py, test.py, main.py
"""

import os
import sys

if len(sys.argv) != 3:
    print("Ипользование: ./find.py <путь к директории> <расширение файлов>")
    exit(1)

dir_path = sys.argv[1]
ext = sys.argv[2]

files = []
for file in os.listdir(dir_path):
    if file.endswith(ext):
        files.append(file)

print(f'Найденные файлы в директории "{dir_path}": {", ".join(files)}')
