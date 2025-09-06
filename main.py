from contact_book import ContactBook


OPTIONS = ('Add Contact', 'View Contacts', 'Search Contacts', 'Update Contacts', 'Delete Contacts', 'Exit')

def main():
    contacts = ContactBook()
    print("__MENU__")
    [print(i+1, option) for i, option in enumerate(OPTIONS)]

    choice = int(input("Enter the number of choice: "))
    if choice == 1:
        add_contact(contacts)
    elif choice == 2:
        get_contacts(contacts)            
    elif choice == 3:
        name = search(contacts)
        print(name)
    elif choice == 4:
        update_name(contacts)
    elif choice == 5:
        delete(contacts)
       


def add_contact(contacts):
    name = input("Enter Contact Name: ")
    phone = input('Enter Phone Number: ')
    email = input('Enter Email: ')
    address = input('Enter Address: ')
    return contacts.add_contact(name, phone, email, address)


def get_contacts(contacts):
    contact_list = contacts.view_contacts()
    return contact_list

def search(contacts):
    name = input("Enter the name to search: ")
    return  contacts.search_contacts(name.lower())


def update_name(contacts):
    oldname = input('Who to update: ')
    # name = contacts.search_contacts(who_to_update.lower())
    # print(name)
    print("Leave the field blank if don't want to update\n(Press Enter to skip)")
    new_name = input('New Name: ')
    new_phone = input('New Phone: ')
    new_email = input('New Email: ')
    new_address = input('New Address')
    
    return contacts.update_contact(oldname, new_name, new_phone, new_email, new_address)


def delete(contacts):
    name = input("Enter Contact Name: ")
    return contacts.delete_contact(name)


if __name__ == "__main__":
    main()