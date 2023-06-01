# Модуль удаления данных в телефонном справочнике

from read_phonebook import *

contacts = read_phonebook()

def delete_contact(contacts):
    print("/ Введите данные контакта, который хотите удалить! /")
    last_name = input("Введите фамилию контакта: ")
    first_name = input("Введите имя контакта: ")

    search_contact = list(filter(lambda x: x["Фамилия"].upper().strip() == last_name.upper().strip() and 
                          x["Имя"].upper().strip() == first_name.upper().strip(), contacts))

    if len(search_contact) != 0:
        print("Найденный контакт:")
        print(str(*search_contact).replace("{", "/ ").replace("}", " /"))
        confirm = input("Вы уверены, что хотите удалить этот контакт? (да/нет): ")

        if confirm.lower() == "да":
            contacts.remove(search_contact[0])
            with open('phonebook.txt', 'w', encoding='utf-8') as data:
                for contact in contacts:
                    contact_data = ', '.join(contact.values()) + '\n'
                    data.write(contact_data)
            print()
            print("/ Контакт успешно удален! /")
        else:
            print()
            print("/ Удаление отменено! /")
    else:
        print()
        print("/ Контакт не найден! /")
