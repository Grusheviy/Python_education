# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

def max_to_min(num):
    list_1 = [randint(1, 4) for _ in range(num)]
    print(list_1)
    min_num = min(list_1)
    max_num = max(list_1)
    for i in range(num):
        if list_1[i] == max_num:
            list_1[i] = min_num
    return list_1   
    
string_length = int(input('Введите кол-во оценок: '))
print(max_to_min(string_length))
