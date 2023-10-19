import random
def get_employees():
    staff = {'John Doe': 10,
             'Jane Doe': 15
             }
    random_employ = random.choice(list(staff.keys()))
    price = staff[random_employ]
    return print(f'У {random_employ} ставка в час {price}')
