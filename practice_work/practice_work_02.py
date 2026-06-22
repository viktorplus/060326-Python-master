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

def remove_empty_lines(filename: str) -> None:
    pass


remove_empty_lines('tasks.txt')
# Пустые строки удалены, сохранено в tasks_cleaned.txt.

remove_empty_lines('t')
# File not found: [Errno 2] No such file or directory: 't'
