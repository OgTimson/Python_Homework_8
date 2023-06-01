# Модуль который показывает все данные в телефонном справочнике

from tabulate import tabulate
from read_phonebook import *

phonebook = read_phonebook()

def display_contacts(phonebook):
    if len(phonebook) == 0:
        print("/ Телефонный справочник пуст! /")
    else:
        table_data = []
        headers = ["Фамилия", "Имя", "Телефон", "Должность"]
        for contact in phonebook:
            row = [contact["Фамилия"], contact["Имя"], contact["Телефон"], contact["Должность"]]
            table_data.append(row)
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
