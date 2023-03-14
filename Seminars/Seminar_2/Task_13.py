# 2) Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих подряд положительных чисел.


# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

from random import randint

n = int(input('Введите число N:'))
counter = 0
counter_last = 0 
for _ in range(n):
    temps = randint(-50, 50)
    print(temps)
    if temps >= 0:
        counter += 1
        counter_first = counter
    elif counter_first > counter_last:
        counter_last = counter
        counter = 0
    else:
        counter = 0
if counter_first > counter_last:
    print('Подряд идущиx положительых чисел:', counter_first)
else:   
    print('Подряд идущиx положительых чисел:', counter_last)