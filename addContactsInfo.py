# def addContact(unique_phone_number,all_contact_info):
#     Phone_Number    =  input('Enter a 11 digit number  : ')
#     Name            =  input('Enter a Name          : ')
#     Email           =  input('Enter a Email         : ')
#     Address         =  input('Enter Address         : ')
#     unique_phone_number.append(Phone_Number)
#     dict =  {
#         'Phone_Number'  :   Phone_Number,
#         'Name'          :   Name,
#         'Email'         :   Email,
#         'Address'       :   Address
#     }
#
#     if unique_phone_number.count(Phone_Number) == 2 :
#         print(f'Phone number: {Phone_Number} already exists. Please try another phone number.')
#     else:
#         all_contact_info.append(dict)
#     return all_contact_info

def addContact(unique_phone_number,all_contact_info):
    Phone_Number    =  input('Enter a 11 digit number   : ').strip()
    Name            =  input('Enter a Name              : ').strip()
    Email           =  input('Enter a Email             : ').strip()
    Address         =  input('Enter Address             : ').strip()

    input_list = []
    if Phone_Number.isdigit() and len(Phone_Number) == 11 and Name[:1].isalpha() and Email[:1].isalpha() and Address[:1].isalnum():
        input_list.append([Phone_Number,Name,Email,Address])
    # if Name[:1].isalpha():
    #     input_list.append(Name)
    # if Email[:1].isalpha():
    #     input_list.append(Email)
    # if Address[:1].isalnum():
    #     input_list.append(Address)
        if len(input_list[0]) == 4:
            dict =  {
                'Phone_Number'  :   Phone_Number,
                'Name'          :   Name,
                'Email'         :   Email,
                'Address'       :   Address
            }
            unique_phone_number.append(Phone_Number)
            if unique_phone_number.count(Phone_Number) == 2:
                print(f'Phone number: {Phone_Number} already exists.\nPlease try another phone number.')
            else:
                all_contact_info.append(dict)
                print('want to add more contact, type: 1 again')
            return all_contact_info

    elif len(Phone_Number) != 11 or not Phone_Number.isnumeric():
        print(f'\nPhone number: {Phone_Number} must be 11 digit and integer and not alphanumeric.\n')
    elif Name =="" or not Name[:1].isalpha():
        print(f'\nName should be start with alphabetical letter.\n')
    elif not Email[:1].isalpha() or Name.isspace():
        print(f'\nEmail should be start with alphabetical letter.\n')

    elif Address == "":
        print(f'\nAddress should not be empty.\n')
    else:
        print('\nError: something happend.\n')





