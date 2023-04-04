def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    sure_name = input('Введите отчество: ')
    phone_number = input('Введите телефон: ')
    with open('D:\\Учеба\\1 четверть\\Python\\Seminars\\Seminar_8\\files\\phone_book.txt', 'a', encoding='utf-8') as data:
        data.write(f"{last_name} {first_name} {sure_name} {phone_number}\n")

def print_data():
    with open('D:\\Учеба\\1 четверть\\Python\\Seminars\\Seminar_8\\files\\phone_book.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search():
    search_name = input('Введите данные: ')
    with open('D:\\Учеба\\1 четверть\\Python\\Seminars\\Seminar_8\\files\\phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

def load_data():
    with open('D:\\Учеба\\1 четверть\\Python\\Seminars\\Seminar_8\\files\\phone_book.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in  text_data:
                    data.write(line)

def ui():
    while True:
        print("1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Вывести все контакты")
        print("4. Записать данные из файла")
        print("5. Выйти из программы")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search()
        elif choice == "3":
            print_data()
        elif choice == "4":
            load_data()
        elif choice == "5":
            break

def main():
    ui()

if __name__ == "__main__":
    main()
