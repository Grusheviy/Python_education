# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return f'No {n} is not prime'
    else:
        return f'Yes {n} is prime'
        
num = int(input('Введите число: '))

print(prime(num))