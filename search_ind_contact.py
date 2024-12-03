def search_by_contact(contacts):
    try:
        if contacts != []:
            search_by_phone = input('Enter 11 digit phone no. to search: ')
            if len(search_by_phone) == 11:
                contacts = [item for item in contacts if item['Phone_Number'] == search_by_phone]
                for contact in contacts:
                    print(f'=================================')
                    print(f'Search result found of phone number: {search_by_phone}')
                    print('details information: ')
                    for key, value in contact.items():
                        print(f'{key:<12}  :  {value}')
                print(f'=================================')
            else:
                print('if not found, check phone no. correct.')
    except Exception as e:
        print("\nContact not Found.")