"""02 Удаление пустых строк

Напишите программу, которая
- удаляет пустые строки из указанного пользователем файла
- и записывает результат в новый файл.

Имя нового файла формируется автоматически по шаблону <oldname>_cleaned.txt.

Если указанный файл не существует, программа должна вывести ошибку.

Используйте файл tasks.txt.

Пример ввода:
Введите имя файла: tasks.txt

Пример вывода:
Пустые строки удалены, сохранено в tasks_cleaned.txt.
"""

import os

def remove_empty_lines(filename: str) -> None:
    if not os.path.isfile(filename):
        print(f'\nFile "{filename}" not found')
        return

    basename, extension = os.path.splitext(filename)

    with open(f'{basename}_cleaned.txt', 'w') as output:
        with open(filename, 'r') as source:
            for line in source:
                if line.strip() != '':
                    output.write(line)

    print('Пустые строки удалены, сохранено в tasks_cleaned.txt.')



remove_empty_lines('tasks.txt')
# Пустые строки удалены, сохранено в tasks_cleaned.txt.

remove_empty_lines('t')
# File not found: [Errno 2] No such file or directory: 't'
