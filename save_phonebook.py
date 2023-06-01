# Модуль сохранения данных из справочника в файле phonebook.csv

import csv
from read_phonebook import *

phonebook = read_phonebook()

def save_phonebook(phonebook):
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as data:
        fieldnames = ["Фамилия", "Имя", "Телефон", "Должность"]
        writer = csv.DictWriter(data, fieldnames=fieldnames)
        writer.writeheader()  # Записываем заголовки
        for contact in phonebook:
            writer.writerow(contact)  # Записываем данные контактов
    print("/ Телефонный справочник сохранен в файле phonebook.csv! /")
