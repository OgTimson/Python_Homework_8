# Модуль добавления данных в телефонный справочник

def add_contact():
    contact = {"Фамилия":input("Введите фамилию: "), "Имя":input("Введите имя: "), 
               "Телефон":input("Введите номер телефона: "), "Должность":input("Введите должность: ")}
    with open('phonebook.txt', 'a', encoding="utf-8") as data:
        values = ', '.join(contact.values())
        data.write(values + '\n')
    print()
    print("/ Контакт успешно добавлен! /")