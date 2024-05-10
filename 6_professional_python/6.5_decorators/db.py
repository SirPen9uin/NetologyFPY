import psycopg2

from singletone import singletone


@singletone
def get_connection():
    return psycopg2.connect(
        host="localhost", database="app", user="app", password="secret", port=5431
    )
