""" 01 Конвертер температуры

Напишите функцию convert_temperature(), которая
- конвертирует температуру из градусов Цельсия в Фаренгейты
- и наоборот.

Формулы для конвертации температур:
Из градусов Цельсия в Фаренгейты:
F=C×95+32F = C \times \frac{9}{5} + 32

Из градусов Фаренгейта в Цельсия: C=(F−32)×59C = (F - 32) \times \frac{5}{9}

Пример вывода:
print(convert_temperature(100, "C"))  # 100C = 212.0F
print(convert_temperature(100, "F"))  # 100F = 37.8C
print(convert_temperature(100, "K"))  # ОШИБКА! Шкала должна быть 'C' или 'F'.
"""


def convert_temperature(temp, scale="C"):
    if scale == "C":
        return temp * 9/5 + 32
    elif scale == "F":
        return (temp - 32) * 5/9

    raise ValueError("ОШИБКА! Шкала должна быть 'C' или 'F'.")


def format_temperature(temp_init, temp_final, scale):
    return f"{float(temp_init):0.1f}{scale} = {float(temp_final):0.1f}{scale}"

cases = [
    (100, "C", 212.0),
    (100, "F", 37.8),
    (100, "K", 212.0),
]

for temp_init, scale, temp_final in cases:
    try:
        converted = convert_temperature(temp_init, scale)
        print(format_temperature(temp_init, converted, scale))
    except ValueError as e:
        print(e)


# def convert_temperature(temp, scale="C"):
#     if scale == "C":
#         return f"{temp}C = {temp * 9/5 + 32:0.1f}F"
#     elif scale == "F":
#         return f"{temp}F = {(temp - 32) * 5/9:0.1f}C"
#     else:
#         return "ОШИБКА! Шкала должна быть 'C' или 'F'."


# print(convert_temperature(100, "C"))  # 100C = 212.0F
# print(convert_temperature(100, "F"))  # 100F = 37.8C
# print(convert_temperature(100, "K"))  # ОШИБКА! Шкала должна быть 'C' или 'F'.
