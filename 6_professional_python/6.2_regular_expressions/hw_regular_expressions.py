import csv
from pprint import pprint as pp
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contact_list = []
# pp(contacts_list)
for contact in contacts_list:
    full_name = ' '.join(contact[:3])
    contact_parts = full_name.split(' ')
    contact_parts = [info for info in contact_parts if len(info) > 0]
    new_contact_list.append(contact_parts)
print(new_contact_list)