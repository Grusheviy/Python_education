# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket = input("Введите номер билета: ")

sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if sum1 == sum2:
    print("Билет счастливый")
else:
    print("Билет не счастливый")


# ticket = input("Введите номер билета: ")
# StrToInt = [int(i) for i in ticket]

# if sum(StrToInt[:3]) == sum(StrToInt[3:]):
#     print("Билет счастливый")
# else:
#     print("Билет не счастливый")