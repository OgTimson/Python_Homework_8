# Модуль поиска контакта по фамилии и имени в справочнике

from read_phonebook import *

contacts = read_phonebook()

def search_contact(contacts):
    last_name = input("Введите фамилию существующего контакта: ")
    first_name = input("Введите имя существующего контакта: ")
    contact = list(filter(lambda x: x["Фамилия"].upper().strip() == last_name.upper().strip() and 
                          x["Имя"].upper().strip() == first_name.upper().strip(), contacts))
    if len(contact) == 0:
        print()
        print("/ Не правильный ввод или такого контакта не существует! /")
    else:
        print()
        print("Найденный контакт:")
        print(str(*contact).replace("{", "/ ").replace("}", " /"))
        print()
