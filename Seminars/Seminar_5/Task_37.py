# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

from random import randint

def row(n):
    if n <= 0:
        return
    num = int(input('Введите последовательность: '))
    row(n - 1)
    print(num, end=' ')
    
    
    
size = int(input('Введите длинну последовательности: '))
row(size)