import csv
import operator
from pprint import pprint as pp
import re
import itertools

def get_contact_dict(file_name):
    with open(file_name, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    new_contact_list = []
    keys = contacts_list[0]
    values = contacts_list[1:]
    for num, vals in enumerate(values):
        new_contact_list.append({})
        for key, val in zip(keys, vals):
            new_contact_list[num].update({key: val})
    return new_contact_list

def phone_format(file_name, new_file_name):
    with open(file_name, encoding="utf-8") as f:
        text = f.read()

    pattern_phone = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    fixed_phones = re.sub(pattern_phone, r'+7(\2)\3-\4-\5\6\7\8', text)
    # return fixed_phones
    with open(new_file_name, 'w+', encoding="utf8") as f:
        text = f.write(fixed_phones)

def name_fixes(file_name):
    contacts_list = get_contact_dict(file_name)
    for contact in contacts_list:
        splited_contact = contact['lastname'].split(' ')
        if len(splited_contact) > 1:
            contact['lastname'] = splited_contact[0]
            contact['firstname'] = splited_contact[1]

        splited_contact = contact['firstname'].split(' ')
        if len(splited_contact) > 1:
            contact['firstname'] = splited_contact[0]
            contact['surname'] = splited_contact[1]
    return contacts_list

def new_contact_book(contacts):
    keys = set(contacts[0].keys())
    groups = ['firstname', 'lastname']
    group = operator.itemgetter(*groups)
    cols = operator.itemgetter(*(keys^set(groups)))
    contacts.sort(key=group)
    grouped_contacts = itertools.groupby(contacts, group)

    contacts_data = []
    for (firstname, lastname), g in grouped_contacts:
        contacts_data.append({'lastname': lastname, 'firstname': firstname})
        for el in g:
            e1 = contacts_data[-1]
            for k, v in el.items():
                if k not in e1 or e1[k] == '':
                    e1[k] = v
    return contacts_data

def write_new_contacts(file_name, dicts):
    keys = list(dicts[0].keys())
    with open(file_name, 'w', encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(keys)
        for dict in dicts:
            datawriter.writerow(dict.values())

if __name__ == '__main__':
    phone_format(file_name='phonebook_raw.csv', new_file_name='fixed_phonebook.csv')
    fixed_names = name_fixes(file_name='fixed_phonebook.csv')
    new_contact_book = new_contact_book(fixed_names)
    write_new_contacts('new_phonebook.csv', new_contact_book)