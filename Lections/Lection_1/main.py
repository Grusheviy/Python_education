# print(5)

# a = 1
# b = 1.11
# n = None  
# print(a)
# print(b)
# print(n)

"""
Многострочный коментарий
a = 1
b = 1.11
n = None  
print(a)
print(b)
print(n)
"""

# n = 'asdasd'
# n1 = "dadada"

# print(n) 
# print(n1)


# n = 5
# n1 = 'dad\'ada' # вывод ковычек в тексте

# print(type(n1),n1) 
# print(type(n), n)

# Интерполяция

# a = 5
# b = 5.89
# c = 'hello'

# print(a,b,c)
# print(a,' - ',b,' - ',c)

# # Через шаблон F строки
# print(f"Через шаблон F строки {a} - {b} - {c}")

# # Через шаблон format
# print("Через шаблон format {} - {} - {}".format(a,b,c))

# Ввод данных

# print('Введите что-то')
# a = input()
# print(f"Результат вашего ввода: {a}")
# b = input('Введите второе что-то: ')

# print(a, "+", b, "=", a + b) # Складываются строки

# Приведение типов

# c = 5.89
# print(type(c))
# print(c)
# n = int(c)
# print(type(n))
# print(n)
# b = str(c)
# print(type(b))
# print(b + 'ase')
# e = bool(c)
# print(type(e))
# print(e)
# # print(b + 'ase')

# print('Введите что-то')
# a = int(input())
# print(f"Результат вашего ввода: {a}")
# b = int(input('Введите второе что-то: '))

# print(a, "+", b, "=", a + b) # Складываются строки

'''
+ Сложение
- Вычитание
* Умножение
/ Деление (по умолчанию в
вещественных числах)
% Остаток от деления
// Целочисленное деление
** Возведение в степень

Приоритет арифметических операций
1. Возведение в степень (**)
2. Умножение (*)
3. Деление (/)
4. Целочисленное деление (//)
5. Остаток от деления (%)
6. Сложение (+)
7. Вычитание (-)

'''

# Округление чисел
# a = 5.15151
# b = 6.141414
# print(round(a*b, 2))
# round()

# Сокращенные присваивания
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

'''
Логические операции:

> Больше
>= Больше или равно
< Меньше
<= Меньше или равно
== Равно (проверяет, равны ли числа)
!= Не равно (проверяет, не равны ли значения)
not Не (отрицание)
and И (конъюнкция)
or Или (дизъюнкция)

a = 1 > 4
print(a) # False

a = 1 < 4 and 5 > 2
print(a) # True

a = 1 == 2
print(a) # False

a = 1 != 2
print(a) # True

Можно сравнивать не только числовые значения, но и строки:
a = 'qwe'
b = 'qwe'
print(a == b) # True

В Python можно использовать тройные и даже четверные неравенства:
a = 1 < 3 < 5 < 10
print (a) # True
'''
# Операторы ветвления if else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Сложные условия
# Сложные условия создаются с помощью логических операторов, таких как: and, or,
# not
'''
if condition1 and condition2: # выполнится, когда оба условия окажутся верными
# operator
if condition3 or condition4: # выполнится, когда хотя бы одно из условий
окажется верным
# operator

n = int(input())
if n % 2 == 0 and n % 3 == 0:
    print('Число кратно 6')
if n % 5 == 0 and n % 3 == 0:
    print('Число кратно 15')
'''
# Управляющие конструкции: while и вариация while-else

# while condition:
# operator 1
# operator 2
# ...
# operator n
'''
n = 423
summa = 0
while summa > 0:
x = n % 10
summa = summa + x
n = n // 10
print(summa) # 9
'''

# Управляющие конструкции: while-else

# while condition:
# operator 1
# operator 2
# ...
# operator n
# else:
# operator n + 1
# operator n + 2
# ...
# operator n + m
'''
i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)
'''

'''
# Пример программного кода без использования break:
n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
else:
    print('Пожалуй')
    print('хватит )')
    print(summa)
# Пожалуй
# хватит )
# 9
'''

'''
Использование флага
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
'''

# Цикл for, range
'''
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20
'''

# Индексы строки
'''
a = 'avwavwva'
print(a[1])

for i in 'qwerty':
    print(i)
'''
# Цикл в цикле
'''
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
'''
# Работа со строками
'''
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
'''

# Команды для работы со строками:
'''
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
1. Определить количество символов в строке:
print(len(text)) # 39
2. Проверить наличие символа в строке (in):
print('ещё' in text) # True
3. Функция, которая делает все буквы строки маленькими:
print(text.lower()) # съешь ещё этих мягких французских булок
4. Функция, которая делает все буквы строки большими:
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
5. Заменить слово на другое :
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок
'''