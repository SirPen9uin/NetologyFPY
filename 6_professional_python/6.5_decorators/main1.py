import requests

from attempts import with_attempts
from db import get_connection
from time_check import time_check


@time_check  # sumator = time_check(sumator)
def sumator(a, b):
    return a + b


@time_check  # get_people = time_check(get_people)
@with_attempts(3, 0)  # get_people = time_check(get_people)
def get_people(person_id):
    return requests.get("https://swapi.dev/api/people/{}".format(person_id)).json()


connection_1 = get_connection()
connection_2 = get_connection()
print(connection_1 is connection_2)
