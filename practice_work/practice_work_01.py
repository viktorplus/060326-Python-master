"""01 Подсчёт частоты слов в файле

Напишите программу, которая
- подсчитывает, сколько раз каждое слово встречается в файле (не учитывая регистр).

Программа запрашивает имя файла и количество популярных слов для вывода.

Если указанный файл не существует, программа должна вывести ошибку.

Используйте файл text.txt.

Пример ввода:
Введите имя файла: text.txt
Введите количество популярных слов: 3

Популярные слова:
the: 27
of: 21
lorem: 17

"""
from collections import Counter
import os

def count_words(file_name: str, num_words: int) -> None:
    if not os.path.isfile(file_name):
        print(f'\nFile "{file_name}" not found')
        return

    with open(file_name, 'r') as f:
        words = f.read().split()

        counter = Counter(words)

        print('Популярные слова:')

        for word, count in counter.most_common(num_words):
            print(f'{word}: {count}')


count_words('text.txt', 3)
# the: 27
# of: 21
# lorem: 17

count_words('t', 3)
# File not found: [Errno 2] No such file or directory: 't'
