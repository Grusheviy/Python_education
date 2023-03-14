# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

a = int(input('Введите число > 1: '))
fib1 = 0
fib2 = 1
count = 2
while fib2 < a:
      fib1, fib2 = fib2, fib1 + fib2
      count += 1
   # print(count)
if a == fib2:
      print(count)
else:  
   print(-1)
