address_book = {}
while True:
    print('*********Address Book***********')
    print('Press 1 to add a contact to book')
    print('Press 2 to display all contacts')
    print('Press 3 to search a contact in address book')
    print('Press 4 to delete a contact from address book')
    print('Press 5 to update a contact')
    print('Press 6 to exit address book')

    choice = int(input('Select yout choice: '))

    if choice == 1:
        name = str(input('Enter contact name').lower())
        phone_number = int(input('Enter your phone number'))
        address = str(input('Enter contact address'))
        address_book[name] = {'name': name, 'phone_number': phone_number, 'address': address}
        print(f'{name} successfully stored in address book')
    elif choice == 2:
        if not address_book:
            print('Address book is empty')
        else:
            print('******All Contacts*****')
            for index, name in enumerate(address_book.keys(), start=1):
                print(f'{index}: {name}')
    elif choice == 3:
        name = str(input('Enter the contact name to search its info').lower())
        if name in address_book:
            print('Contact Details:')
            print(f'Name: {name}')
            print(f'Contact Number: ',address_book[name]['phone_number'])
            print(f'Address: ',address_book[name]['address'])
        else:
            print('The name is not in found address book')
    elif choice == 4:
        name = str(input('Enter the contact name to delete its info').lower())
        if not address_book:
            print('Address book is empty')
        else:
            if name in address_book:
                del address_book[name]
                print(f'{name} is no more in the address book')
            else:
                print(f'{name} does not exist in the address book')
    elif choice == 5:
        name = str(input('Enter the contact name to delete its info').lower())
        if not address_book:
            print('Address book is empty')
        else:
            if name in address_book:
                phone = input('Enter the updated phone number (Press Enter if you dont want to update number)')
                address = input('Enter the updated address number (Press Enter if you dont want to update address)')
                if phone:
                    address_book[name]['phone_number'] = phone
                if address:
                    address_book[name]['address'] = address
                print(f'{name} is updated in the address book')
            else:
                print(f'{name} does not exist in the address book')

    elif choice == 6:
        print('Thanks for using address book app')
        break
