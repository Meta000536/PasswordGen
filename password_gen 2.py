# password_gen.py
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits  # letters + digits
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Your password: {password}")

generate_password()