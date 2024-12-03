import json
import os

def contacts():
    try:
        if os.path.exists('contacts.json'):
            with open('contacts.json','r') as file:
                contacts = json.load(file)
            return contacts
        else:
            return "empty, populate first."

    except Exception as e:
        print('Contact data is not exists. populate first')
