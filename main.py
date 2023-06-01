# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (например, имя или фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя 
# или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

from add_contact import *
from search_contact import *
from update_contact import *
from delete_contact import *
from read_phonebook import *
from display_contacts import *
from save_phonebook import *

while True:
    print("Меню справочника:")
    print("1. Добавить новый контакт")
    print("2. Изменить существующий контакт")
    print("3. Поиск контакта")
    print("4. Удаление контакта")
    print("5. Вывести контакты на экран")
    print("6. Сохранить справочник")
    print("0. Выход")
    print()

    choice = input("Введите номер операции: ")

    if choice == "1":
        print()
        add_contact()
        print()
    elif choice == "2":
        print()
        update_contact(contacts)
        print()
    elif choice == "3":
        print()
        search_contact(contacts)
        print()
    elif choice == "4":
        print()
        delete_contact(contacts)
        print()
    elif choice == "5":
        print()
        display_contacts(phonebook)
        print()
    elif choice == "6":
        print()
        save_phonebook(phonebook)
        print()
    elif choice == "0":
        print()
        print("/ Выход из меню. До свидания! /")
        break
    else:
        print("/ Неверный выбор операции! /")
