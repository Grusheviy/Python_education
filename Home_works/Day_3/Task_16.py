# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

n = int(input('Введите длинну массива N: '))
x = int(input('Введите искомое число X: '))
count = 0
list_1 = [randint(1, 5) for i in range(n)]
print(*list_1)
for i in list_1:
    if i == x:
        count += 1
print(f'Число X встречается: {count} раз')