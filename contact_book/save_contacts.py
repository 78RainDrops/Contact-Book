import json, os
from pathlib import Path

path = Path.home()/'contacts.json'

def save_contacts(contact_list):
    contact_dict = {'contacts' : contact_list}
    path.write_text(json.dumps(contact_dict, indent=4))
