# password_gen.py
import random
import string

def generate_password(length):
    if length <= 0:
        raise ValueError("Длина должна быть положительной")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Введите длину пароля: "))
    print(f"Ваш пароль: {generate_password(length)}")
except ValueError as e:
    print(f"Ошибка: {e}")