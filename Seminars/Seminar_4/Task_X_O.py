# Крестики нолики

field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_field(field):
    print(*field[:3])
    print(*field[3:6])
    print(*field[6:])

def win_check(field):
    # Исправлены ошибки в проверке победы
    if (field[0] == field[1] == field[2]
    or field[3] == field[4] == field[5]
    or field[6] == field[7] == field[8]
    or field[0] == field[3] == field[6]
    or field[1] == field[4] == field[7]
    or field[2] == field[5] == field[8]
    or field[0] == field[4] == field[8] 
    or field[2] == field[4] == field[6]):
        return True
    return False

print_field(field)

for step in range(1, 10):
    print('Ход:', step)
    move = input("Введите координаты хода: ")
    valid_move = False
    while move not in field:
        move = input("Введите корректные координаты хода: ")
    else:
        valid_move = True
    if step % 2 != 0:
        symbol = 'X'
        field[int(move)-1] = symbol
    else:
        symbol = 'O'
        field[int(move)-1] = symbol
    print_field(field)
    # Проверяем победу после каждого хода
    if win_check(field):
        print(f'Победил игрок {symbol}')
        break
else:
    # Если цикл for закончился без вызова break, значит произошла ничья
    print("Ничья!")




    

   