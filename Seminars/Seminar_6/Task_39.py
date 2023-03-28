# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

from random import randint

def find_unique_elements(first_list, second_list):

    unique_elements = []
    for element in first_list:
        if element not in second_list:
            unique_elements.append(element)
    return unique_elements


size_list_1 = int(input("Введите количество элементов в первом массиве: "))
first_list = [randint(1, 10) for _ in range(size_list_1)]

size_list_2 = int(input("Введите количество элементов во втором массиве: "))
second_list = [randint(1, 10) for _ in range(size_list_2)]

print(*find_unique_elements(first_list, second_list), sep='\n')


# from random import randint
# num_1=int(input("Введите размер первого массива: "))
# num_2=int(input("Введите размер второго массива: "))
# array_1=[randint(1,10) for _ in range(num_1)]
# array_2=[randint(1,10) for _ in range(num_2)]
# result_array=[elem for elem in array_1 if elem not in array_2]
# print(array_1)
# print(array_2)
# print(result_array)