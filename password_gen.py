# password_gen.py
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters  # буквы (a-z, A-Z)
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Ваш пароль: {password}")

generate_password()