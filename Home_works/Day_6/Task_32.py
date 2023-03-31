# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

total_elems = int(input('Введите количество элементов массива: '))

list_1 = [randint(1, 10) for _ in range(total_elems)]
print(list_1)

min_range = int(input('Введите минимальный элемент искомого диапазона: '))
max_range = int(input('Введите максимальный элемент искомого диапазона: '))

# for index, elem in enumerate(list_1):
#     if min_range <= elem <= max_range:
#         print(index)
        
print(*[index for index, elem in enumerate(list_1) if min_range <= elem <= max_range])