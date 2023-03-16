# Как работать со списками?
# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка

'''
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1)
print(*list_1) # Вывод списка без квадратных скобок

for i in list_1:
    print(i)

print(len(list_1)) # Выводит длинну списка
print(list_1[0]) # Выводит элемент списка по его индексу -1 индексация с конца

list_2 = [1, 5]
print(list_2)
list_2.append(8) # .append добавляет элемент в список
print(list_2)

'''

# Создаем пустой список, заполняем его значениями i
'''
list_1 = []
print(list_1)
for i in range(5): # range() добавляет значения от 0 до 5 - 1
    list_1.append(i)
    print(list_1)
'''
 
# Удаление последнего элемента списка.
# Метод pop удаляет последний элемент из списка:
'''
list_1 = [12, 7, -1, 21, 0]
a = list_1.pop()
print(a)
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]
'''

# Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
'''
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0]
'''

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
'''
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11)) # Первый аргумент позиция куда вставить, второй аргумент Значение
print(list_1) # [12, 7, 11, -1, 21, 0]
'''

# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк? Также существует срез
# списка, давайте научимся изменять наш список
#  Отрицательное число в индексе — счёт с конца списка
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7] Идем с начала списка, до конца с шагом 6
print(list_1[::6]) # [1, 7] Идем с начала списка, до конца с шагом 6
'''

# Кортежи
# 💡 Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
# каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
# меньше места в памяти и работают быстрее
'''
t = ()
print(type(t))

t = (1)
print(type(t)) 

t = (1,)
print(type(t))


colors = ['red', 'green', 'blue']
print(type(colors))
print(colors) # ['red', 'green', 'blue']
colors = tuple(colors)
print(type(colors))
'''
'''
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print(f'r:{red} g:{green} b:{blue}') 
'''
t = (1, 2, 3, 4, 5,)
print(t[1])
'''
for i in t:
    print(i)
'''
'''
for i in range(len(t)):
    print(t[i])
'''
'''
t[0] = 2
print(t) # Будет ошибка тк t = tuple
'''

# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для
# определения элемента используется значение ключа (строка, число).
'''
dictionary = {}
d = dict()
d['q'] = 'qwerty'
print(d)
d['w'] = 'werty'
print(d['q'])
'''

'''
dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'

# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'

del dictionary['left'] # удаление элемента

for item in dictionary: # for (k,v) in dictionary.items(): k - key, v - value
    print('{}: {}'.format(item, dictionary[item])) # Выводит пару (Ключ - значение)
# up: ↑
# down: ↓
# right: →

dictionary[895] = 58585
print(dictionary)
'''

# Множества
# 💡 Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два
# множества, Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность. Давайте разберем их.
'''
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()
'''

# Операции со множествами в Python
'''
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5} Пересечения значения в множествах
dl = a.difference(b) # dl = {1, 3} Разность a - b остаются значения из а 
dr = b.difference(a) # dr = {13, 21} Разность b - a остаются значения из b
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} Находим пересечения а,b зачем а объединяем с b 
# и находим разность объединения a,b с пересечением а,b  

# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления.

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
'''

# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.
'''
# Простая ситуация — список:
# list_1 = [exp for item in iterable]
# 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
print(list_1)
print()
# Добавить условие (только чётные числа)
list_2 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
print(list_2)
print()
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_3 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
print(list_3)
print()
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_4 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_4) # [0, 4, 8, 12, 16]
'''

# Самые распространенные ошибки:
# SyntaxError(Синтаксическая ошибка)

'''
number_first = 5
number_second = 7
if number_first > number_second # !!!!!
print(number_first)
# Отсутствие :
'''
'''
IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
print(number_first) # !!!!!
# Отсутствие отступов
'''
'''
# TypeError(Типовая ошибка)
text = 'Python'
number = 5
print(text + number)
# Нельзя складывать строки и числа
'''
'''
# ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя
'''
'''
# KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует
'''
'''
# NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)
# Переменной names не существует
'''
'''
# ValueError(Ошибка значения)
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения
'''
