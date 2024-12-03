import addContactsInfo
import saveToFile
import view_all_contact
import load_from_contacts
import remove_from_contact
import search_ind_contact

all_contact_info = []
unique_phone_number = []
print('Welcome to contact book managenent system')


while True:
    print('0: Exit.')
    print('1: Add Contatct')
    print('2: Save Contact to File')
    print('3: View all Contact')
    print('4: Load from File')
    print('5: Remove one contact from contact list.')
    print('6: Search a contact by phone number with details.')

    choice = input('\nType your choice:  ')
    if choice == '0':
        print('\nThanks for using Contact Book Management System.')
        break
    elif choice == '1':
        addContactsInfo.addContact(unique_phone_number,all_contact_info)
    elif choice == '2':
        saveToFile.saveAsJson(all_contact_info)
        print('Contact saved to file succesfully.')
    elif choice == '3':
        view_all_contact.view_contacts()
    elif choice == '4':
        data = load_from_contacts.contacts()
        if data == None:
            print('Contact list are empty.')
        else:
            print(f'\nThe loaded contacts from file are: \n{data}\n')
    elif choice == '5':
        contacts = load_from_contacts.contacts()
        new_contact = remove_from_contact.remove_by_contact(contacts)
        saveToFile.saveAsJson(new_contact)
    elif choice == '6':
        contacts = load_from_contacts.contacts()
        search_ind_contact.search_by_contact(contacts)
        print('')
    else:
        print('Please choose a valid choice.')

