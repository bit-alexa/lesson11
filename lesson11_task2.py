# Task 2 Extend Phonebook application
import json


def load_func(phone_book):
    try:
        with open(phone_book) as f:
            data = json.load(f)
        return data
    except:
        print('No such phonebook')


def add_new(data):
    first_name = input('Input first name: ')
    last_name = input('Input last name: ')
    phone = input('Input phone: ')
    adress = input('Input city or state: ')
    data.append([first_name, last_name, phone, adress])
    return(data)


def close_app(data):
    with open(phone_book, 'w') as file:
        json.dump(data, file)


def search(data):
    param = input('Please, write what we are searching by: 0 for first name, 1 for last name, 2 for phone, 3 for city, 4 for full name: ')
    request = input('Write data what we a searching: ')
    if param == '4':
        fname = request.split(' ')[0]
        lname = request.split(' ')[1]
        return [name for name in data if name[0] == fname and name[1] == lname][0]
    else:
        return [name for name in data if name[int(param)] == request][0]

def delete_data(data, phone):
    index = data.index([name for name in data if name[2] == phone][0])
    data.pop(index)
    return data

def update_data(data, phone):
    delete_data(data, phone)
    first_name = input('Input first name: ')
    last_name = input('Input last name: ')
    adress = input('Input city or state: ')
    data.append([first_name, last_name, phone, adress])
    return(data)


if __name__ == '__main__':
    phone_book = 'phonebook.json'
    data = load_func(phone_book)
    while True:
        print(data)
        choise = int(input('What do you want to do? \n1 Add new entries \n2 Search by info about user \n'
              '3 Delete a record for a given telephone number \n4 Update a record for a given telephone number \n'
              '5 for exit the program\nCHOISE: '))
        if choise == 5:
            close_app(data)
            break
        elif choise == 1:
            add_new(data)
            print(data)
        elif choise == 2:
            searched = search(data)
            if searched == []:
                print('No such data yet')
            else:
                print(searched)
        elif choise == 3:
            phone = input('Please, write the phone: ')
            try:
                delete_data(data, phone)
            except:
                print('No such phone')
        elif choise == 4:
            phone = input('Please, write the phone: ')
            try:
                update_data(data, phone)
            except:
                print('No such phone')
