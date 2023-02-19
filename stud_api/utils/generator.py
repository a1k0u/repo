import string
import random

ELEMENTS = string.ascii_letters + string.digits


def password_generate():
    return "".join([random.choice(ELEMENTS) for _ in range(8)])


def email_generate():
    return f"{''.join([random.choice(ELEMENTS) for _ in range(8)])}@mail.ru"
