import json

def view_contacts():
    try:
        with open('contacts.json','r') as file:
            contacts = json.load(file)

            print(f'\ndetails of individual contact.')
        for contact in contacts:
            print(f'--------------------------------------')
            for key,value in contact.items():
                print(f'{key:<12}  :  {value}')
            print(f'--------------------------------------\n')
    except Exception as e:
        print(f'\nContact list are empty. Populate first.\n')
