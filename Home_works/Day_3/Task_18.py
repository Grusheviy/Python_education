# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

string_length = int(input('Введите длину массива N: '))
find_num = int(input('Введите искомое число X: '))
list_1 = [randint(1, 10) for _ in range(string_length)]
print(list_1)

min_diff = abs(find_num - list_1[0])
min_num = list_1[0]

for i in range(1, len(list_1)):
    current_diff = abs(find_num - list_1[i])
    if current_diff < min_diff:
        min_diff = current_diff
        min_num = list_1[i]

print(f'Наиболее близкое по величине к числу {find_num} число: {min_num}')