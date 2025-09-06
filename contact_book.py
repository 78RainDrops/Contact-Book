import json
from contact import Contact

class ContactBook:
    def __init__(self,filename="contacts.json") -> None:
        self._contacts = {}
        self.filename = filename
        self.load_contact()


    def add_contact(self, name, phone, email, address):
        name_key = name.lower()
        if name_key in self.contacts:
            raise ValueError("Contact already exists!")

        contact = Contact(name, phone, email, address)
        self.contacts[name_key] = contact
        self.save_contact()

        return contact

    @property
    def contacts(self):
        return self._contacts["contacts"]
    
    def view_contacts(self):
        for contact in self.contacts.values():
            print(contact)


    def search_contacts(self, name):
        name_key = name.lower
            # return Contact(name, info["phone"], info["email"], info["address"])
        return self._contacts.get(name_key, None)
        pass


    def update_contact(self,oldname, name=None, phone=None, email=None, address=None):
        oldkey = oldname.lower()
        contact = self.contacts.get(oldkey)
        
        if not contact:
            print("Contact not Found")
            return False
        
        contact.update(name, phone, email, address)
        if name and name.lower() != oldkey:
            self.contacts[name.lower()] = self.contacts.pop(oldkey)

        self.save_contact()
        return True


    def save_contact(self):
        data = {
            'contacts': {
                name: c.to_dict() 
                for name, c in self.contacts.items()
            }
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)


    def delete_contact(self, name):
        namekey = name.lower()
        if namekey in self.contacts:
            del self.contacts[namekey]
            self.save_contact()
            print('Delete Successfully')
            return True
        else:
            print(f"Contact {namekey} not found ")
            return False


    def load_contact(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
                self._contacts['contacts'] = {
                    name: Contact.from_dict(name, info) 
                    for name, info in data.get('contacts',{}).items()
                }

        except FileNotFoundError:
            pass
    
    def debug_types(self):
        for name, val in self.contacts.items():
            print(type(name), type(val))
