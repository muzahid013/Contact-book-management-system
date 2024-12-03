import json

def saveAsJson(all_contact_info):
    with open('contacts.json','w') as file:
        json.dump(all_contact_info,file,sort_keys=True,indent=4,ensure_ascii=False)
