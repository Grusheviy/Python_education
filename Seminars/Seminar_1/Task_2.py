a = int(input('Количество учащихся в классе А: '))
b = int(input('Количество учащихся в классе B: '))
c = int(input('Количество учащихся в классе C: '))

students1 = a // 2 + a % 2
students2 = b // 2 + b % 2
students3 = c // 2 + b % 2
total_students = students1 + students2 + students3
print(total_students)
