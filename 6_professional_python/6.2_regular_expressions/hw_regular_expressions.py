import csv
import re
import operator
import itertools


def read_csv_to_dict(file_name):
    contacts_dict = []
    with open(file_name, encoding="utf8") as f:
        reader = csv.reader(f, delimiter=",")
        contacts_list = list(reader)
        keys = contacts_list[0]
        values = contacts_list[1:]
        for num, vals in enumerate(values):
            contacts_dict.append({})
            for key, val in zip(keys, vals):
                contacts_dict[num].update({key: val})
        return contacts_dict


def fix_phones(text):
    pattern_phone = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    fixed_phones = re.sub(pattern_phone, r'+7(\2)\3-\4-\5\6\7\8', text)
    return fixed_phones


def fix_names(contacts_dict):
    for v in contacts_dict:
        splt = v['lastname'].split(' ')
        if len(splt) > 1:
            v['lastname'] = splt[0]
            v['firstname'] = splt[1]
            if len(splt) > 2:
                v['surname'] = splt[2]
        splt = v['firstname'].split(' ')
        if len(splt) > 1:
            v['firstname'] = splt[0]
            v['surname'] = splt[1]
    return contacts_dict


def merge_names(contacts):
    all_keys = set(contacts[0].keys())
    group_list = ['firstname', 'lastname']
    group = operator.itemgetter(*group_list)
    cols = operator.itemgetter(*(all_keys ^ set(group_list)))
    contacts.sort(key=group)
    grouped = itertools.groupby(contacts, group)

    merge_data = []
    for (firstname, lastname), g in grouped:
        merge_data.append({'lastname': lastname, 'firstname': firstname})
        for gr in g:
            d1 = merge_data[-1]
            for k, v in gr.items():
                if k not in d1 or d1[k] == '':
                    d1[k] = v
    return merge_data


if __name__ == '__main':
    with open("phonebook_raw.csv", encoding="utf8") as f:
        text = f.read()

    fixed_phones_text = fix_phones(text)
    fixed_phones_contacts = read_csv_to_dict(fixed_phones_text)
    merged_contacts = merge_names(fix_names(fixed_phones_contacts))

    with open("phonebook.csv", "w", encoding="utf8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=merged_contacts[0].keys())
        writer.writeheader()
        writer.writerows(merged_contacts)
