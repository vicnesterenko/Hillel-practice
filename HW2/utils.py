import string
import random


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits

    result = ''
    for _ in range(length):
        result += random.choice(chars)

    return result
