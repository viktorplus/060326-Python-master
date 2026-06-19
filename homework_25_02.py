""" 02 Логирование ошибок

Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log
в соответствии с форматом ниже.

ВАЖНО: используйте вывод ошибок
    - и в файл,
    - и на экран.

Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

"""

import logging

pass

def safe_division(dividend, divisor):
    pass

# Пример вызова функции
safe_division('a', 5)       # False
safe_division(5, 0)         # False
safe_division(5, 2)         # True
safe_division('5.5', '1.2') # True

# 2025-11-07 11:41:34,147 - ERROR - homework_33_02.py - 48 - Ошибка: Введено некорректное число: could not convert string to float: 'a'
# 2025-11-07 11:41:34,148 - ERROR - homework_33_02.py - 50 - Ошибка: Деление на ноль невозможно: float division by zero
# Результат: 2.5
# Результат: 4.583333333333334
