# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# from random import randint

# string_1_length = int(input('Введите длину массива N: '))
# list_1 = {randint(1, 10) for _ in range(string_1_length)}
# string_2_length = int(input('Введите длину массива N: '))
# list_2 = {randint(1, 10) for _ in range(string_2_length)}
# print(*list_1)
# print(*list_2)
# list_res = []

# for num_1 in list_1:
#     for num_2 in list_2:
#         if num_1 == num_2:
#             list_res.append(num_1)
                   
# sorted = len(list_res)
# for i in range(sorted):
#     for j in range(0, sorted-i-1):
#         if list_res[j] > list_res[j+1]:
#             list_res[j], list_res[j+1] = list_res[j+1], list_res[j]
# print(*list_res)

# Решение через .intersection и подсмотренный метод sorted
from random import randint

string_1_length = int(input('Введите длину массива N: '))
list_1 = {randint(1, 10) for _ in range(string_1_length)}

string_2_length = int(input('Введите длину массива N: '))
list_2 = {randint(1, 10) for _ in range(string_2_length)}

print(*list_1)
print(*list_2)

list_res = sorted(list_1.intersection(list_2))

print(*list_res)