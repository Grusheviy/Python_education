# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:   Вывод:
# 300     220 284


def get_sum_div(n):
    div_sum = 0
    for i in range(1, n):
        if n % i == 0:
            div_sum += i
    return div_sum
            
k = int(input("Введите количество элементов в массиве: "))

friendly_num = []
for i in range(1, k):
    div_sum = get_sum_div(i)
    if div_sum > i and div_sum <= k and get_sum_div(div_sum) == i:
        pair = (i, div_sum)
        if pair not in friendly_num:
            friendly_num.append(pair)
print(*pair)
        
        
# def sum_del(num):
#     sum_a = 0
#     for el in range(1, int(num**0.5 + 1)):
#         if num % el == 0:
#             sum_a += el + num // el
#     return sum_a


# k = int(input('введите k: '))
# for first_num in range(1, k):
#     second_num = sum_del(first_num)
#     if sum_del(second_num) == first_num and first_num != second_num and first_num > second_num:
#         print(first_num, second_num)