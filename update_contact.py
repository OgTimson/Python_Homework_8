# Модуль изменения данных в телефонном справочнике

from read_phonebook import *

contacts = read_phonebook()

def update_contact(contacts):
    print("/ Введите данные контакта, который хотите изменить! /")
    last_name = input("Введите фамилию существующего контакта: ")
    first_name = input("Введите имя существующего контакта: ")
    search_contact = list(filter(lambda x: x["Фамилия"].upper().strip() == last_name.upper().strip() and 
                          x["Имя"].upper().strip() == first_name.upper().strip(), contacts))
    if len(search_contact) != 0:
        print(str(*search_contact).replace("{", "/ ").replace("}", " /"))
        print("Изменение данных...")
        for i, contact in enumerate(contacts):
            if contact == search_contact[0]:
                new_contact = {"Фамилия":input("Введите новую фамилию: "),
                               "Имя":input("Введите новое имя: "),
                               "Телефон":input("Введите новый номер телефона: "),
                               "Должность":input("Введите новую должность: ")}
                contacts[i] = new_contact
                break
        with open('phonebook.txt', 'w', encoding='utf-8') as data:
            for contact in contacts:
                contact_data = ', '.join(contact.values()) + '\n'
                data.write(contact_data)
        print()
        print("/ Контакт успешно изменен! /")
    else:
        print()
        print("/ Не правильный ввод или такого контакта не существует! /")
