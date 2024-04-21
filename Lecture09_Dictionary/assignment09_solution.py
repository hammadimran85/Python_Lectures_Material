Phone_Book = {}

while True:
    print('Welcome to Address Book System')
    print('Press 1 to Add Contact')
    print('Press 2 to Display All Contacts')
    print('Press 3 to Delete Contact')
    print('Press 4 to Update Contact')
    print('Press 5 to Search Contact')
    print('Press 6 to Exit')

    choice = int(input('Enter your choice (1/2/3/4/5/6): '))

    if choice == 1:
        name = input('Enter your name: ')
        phone = input('Enter your phone: ')
        address = input('Enter your address: ')

        new_contact = {'name': name, 'phone_number': phone, 'address': address}

        Phone_Book[name] = new_contact
        print('---------------------------------')
        print('Contact Added Successfully...!')
        print('---------------------------------')

    if choice == 2:
        print('---------------------------------')
        for key in Phone_Book.keys():
            print('---------------------------------')
            print('Name: ',Phone_Book[key]['name'].upper())
            print('Phone Number: ', Phone_Book[key]['phone_number'])
            print('Address: ', Phone_Book[key]['address'].upper())
            print('---------------------------------')

        print('---------------------------------')

    if choice == 3:
        name = input('Enter name to delete its Data')
        if name in Phone_Book:
            del Phone_Book[name]
            print('---------------------------------')
            print('Contact Deleted Successfully...!')
            print('---------------------------------')
        else:
            print('---------------------------------')
            print('Name not Found')
            print('---------------------------------')

    if choice == 4:
        name = input('Enter name to update its Data')
        if name in Phone_Book:
            updated_phone = input('Enter updated phone number: ')
            updated_address = input('Enter updated address: ')

            if updated_phone:
                Phone_Book[name]['phone_number'] = updated_phone

            if updated_address:
                Phone_Book[name]['address'] = updated_address

            print('---------------------------------')
            print('Contact Updated Successfully...!')
            print('---------------------------------')
        else:
            print('---------------------------------')
            print('Name not Found..!')
            print('---------------------------------')

    if choice == 5:
        name = input('Enter name to Search its Data: ')

        if name in Phone_Book:
            print('---------------------------------')
            for key, value in Phone_Book[name].items():
                print(key.upper()+': ',value.upper())
            print('---------------------------------')
    
    if choice == 6:
        print('---------------------------------')
        print('Thanks for using Address Book!')
        print('---------------------------------')
        break
