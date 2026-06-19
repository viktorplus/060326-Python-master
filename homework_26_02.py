""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys


def find_files_with_extension(directory, extension):
    """Рекурсивно ищет файлы с заданным расширением."""
    pass


# Предварительно создаём ненужные файлы для удаления
files = [
    'error.log',
    'system.log',
    'old.log',
    'debug.log',
]

for file in files:
    with open(file, 'w') as f:
        f.write("")




