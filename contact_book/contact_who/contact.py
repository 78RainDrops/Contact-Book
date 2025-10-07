import argparse

def initializer():
    contact_list = [
        {'name' : 'name',
        'address' : 'address',
        'email' : 'email',
        'phone' : 'phone'}
    ]
    contact_id = 0
    return contact_list, contact_id
    ...

def add_contacts(contact_list, contact_id):
    contact_id += 1
    contact_form = fill_up_form()
    contact_list.append(contact_form)
    print("Contact added successfully")
    list_contacts(contact_list)
    return contact_list

def fill_up_form():
    name = input("Enter Name: ")
    address = input("Address: ")
    email = input("Enter Email: ")
    phone = input("Phone: ")
    
    info = {
        'name' : name,
        'address' : address,
        'email' : email,
        'phone' : phone
    }
    
    return info

def list_contacts(contact_list, searched=None):
    for contact in contact_list:
        print(f"Name: {contact['name']} | Address: {contact['address']} | Email: {contact['email']} | Phone: {contact['phone']}")

def main():
    contact_list, contact_id = initializer()
    parser = argparse.ArgumentParser(description="Contacts storage")
    subparser = parser.add_subparsers(dest='command')
    
    add_parser = subparser.add_parser('add', help='Add contacts')

    list_parser = subparser.add_parser('list', help='List all the contacts')
    list_parser.add_argument('-s', '--search', help='Search names in the contacts')

    args = parser.parse_args()
    if args.command == 'add':
        add_contacts(contact_list, contact_id)
    elif args.command == 'list':
        if args.search:
            list_contacts(contact_list)
        else:
            list_contacts(contact_list)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()