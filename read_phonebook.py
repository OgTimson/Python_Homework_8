# Модуль чтения существующих данных из справочника

def read_phonebook():
    contacts = []
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            values = line.strip().split(', ')
            contact = {
                "Фамилия":values[0],
                "Имя":values[1],
                "Телефон":values[2],
                "Должность":values[3]
            }
            contacts.append(contact)
    return contacts
