def remove_by_contact(contacts):
    try:
        if contacts != []:
            print(f'Before remove, contacts: \n{contacts}')
            remove_by_phone = input('Ensure 11 digit phone no. to remove: ')
            new_contacts = [item for item in contacts if item['Phone_Number'] != remove_by_phone]
            if len(new_contacts) < len(contacts):
                print(f'after remove, contacts: \n{new_contacts}')
                return new_contacts
    except Exception as e:
        print("Contact not Found.")