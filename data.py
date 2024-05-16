import random
import string


def generate_payload_for_create_courier():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


def generate_payload_for_create_order():
    payload = {
        "firstName": "Boris",
        "lastName": "Britva",
        "address": "422 Park Road, London",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Bullet-Dodger",
        "color": ["BLACK"]
    }
    return payload
