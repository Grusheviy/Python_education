# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

n = int(input('Введите длинну массива N: '))
x = int(input('Введите искомое число X: '))
list_1 = [randint(1, 10) for i in range(n)]
# list_1 = [1, 2, 3, 4, 5, 15]
print(list_1)

closest_min = list_1[0]
closest_max = list_1[0]

for i in list_1:
    diff = x - i
    if diff < closest_min:
        closest_min = diff
        closest_min = i
    elif diff > closest_max:
        closest_max = diff
        closest_max = i

print(f'Ближайшие к искомому {x} : {closest_min, closest_max}')