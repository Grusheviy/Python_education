def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    sure_name = input('Введите отчество: ')
    phone_number = input('Введите телефон: ')
    with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'a', encoding='utf-8') as data:
        data.write(f"{last_name} {first_name} {sure_name} {phone_number}\n")
        print('----------------') 

def print_data():
    with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'r', encoding='utf-8') as data:
        print('----------------') 
        print(data.read())
        print('----------------') 

def search():
    search_name = input('Введите данные: ')
    with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)
                print('----------------') 


def load_data():
    with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        print('----------------')
        path = input('Введите адрес файла: ')
        print('----------------')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in  text_data:
                    data.write(line)
            print('----------------')


# ДОМАШНЕЕ ЗАДАНИЕ Day_8 Task_38
def update_contact():
    search_name = input('Введите данные контакта, Фамилию Имя или Отчетсво: ')
    with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'r+', encoding='utf-8') as data:
        lines = data.readlines()
        for i, line in enumerate(lines):
            if search_name in line:
                print('----------------')
                print(f'Старые данные: {line}')
                print('----------------')
                last_name, first_name, sure_name, phone_number = line.split()
                new_last_name = input('Введите новую фамилию (или оставьте пустым, чтобы оставить старое): ')
                new_first_name = input('Введите новое имя (или оставьте пустым, чтобы оставить старое): ')
                new_sure_name = input('Введите новое отчество (или оставьте пустым, чтобы оставить старое): ')
                new_phone_number = input('Введите новый телефон (или оставьте пустым, чтобы оставить старый): ')
                if new_last_name:
                    last_name = new_last_name
                if new_first_name:
                    first_name = new_first_name
                if new_sure_name:
                    sure_name = new_sure_name
                if new_phone_number:
                    phone_number = new_phone_number
                lines[i] = f"{last_name} {first_name} {sure_name} {phone_number}\n"
                data.seek(0)
                data.truncate(0)
                data.writelines(lines)
                print('----------------')
                print('Данные успешно изменены')
                print('----------------')
                with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'w', encoding='utf-8') as data:
                    data.writelines(lines)            
                break
        else:
            print('----------------')
            print('Контакт не найден')
            print('----------------')
        ui()


# ДОМАШНЕЕ ЗАДАНИЕ Day_8 Task_38
def delete_contact():
    search_name = input('Введите данные контакта, Фамилию Имя или Отчетсво: ')
    with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'r+', encoding='utf-8') as data:
        lines = data.readlines()
        for i, line in enumerate(lines):
            if search_name in line:
                print('----------------')
                print(f'Удален контакт: {line}')
                print('----------------')
                del lines[i]
                break
        else:
            print('----------------')
            print('Контакт не найден')
            print('----------------')
        with open('D:\\Учеба\\1 четверть\\Python\\Home_works\\Day_8\\files\\phone_book.txt', 'w', encoding='utf-8') as data:
            data.writelines(lines)
        ui()

def ui():
    while True:
        print('----------------')
        print('1. Добавить контакт')
        print('2. Поиск контакта')
        print('3. Вывести все контакты')
        print('4. Записать данные из файла')
        print('5. Обновить данные контакта')
        print('6. Удалить контакт')
        print('7. Выйти из программы')
        print('----------------')

        choice = input('Выберите действие: ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            search()
        elif choice == '3':
            print_data()
        elif choice == '4':
            load_data()
            # ДОМАШНЕЕ ЗАДАНИЕ Day_8 Task_38
            
        elif choice == '5':
            update_contact()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            print('----------------')
            print('ВСЕГО ХОРО-ШЕГО')
            break
