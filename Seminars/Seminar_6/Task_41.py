# Задача №41. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

from random import randint

def find_min_max(list_1):
    count = 0    
    for element in range(1, len(list_1) - 1):
        if list_1[element - 1] < list_1[element] > list_1[element + 1]:
            count += 1
    return count

n = int(input("Введите количество элементов в массиве: "))
list_1 = [randint(1, 5) for _ in range(n)]
print(list_1)

# list_1 = []
# for i in range(n):
#     element = int(input(f"Введите элемент {i + 1} массива: "))
#     list_1.append(element)
print(find_min_max(list_1))

# from random import randint

# size_arr = randint(5, 9)
# print(size_arr)
# arr = [randint(1, 10) for _ in range(size_arr)]
# print(arr)

# count = 0
# for i in range(1, size_arr-1):
#     if arr[i-1] < arr[i] > arr[i+1]:
#         count += 1
# print(count)