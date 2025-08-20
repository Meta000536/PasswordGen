# password_gen.py
import random
import string
import re

def check_strength(password):
    """Проверяет надежность пароля по длине и типам символов."""
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    return "Сильный" if score >= 3 else "Слабый" if score <= 1 else "Средний"

def generate_password(length, use_letters=True, use_digits=False, use_symbols=False):
    if length <= 0:
        raise ValueError("Длина должна быть положительной")
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("Выберите хотя бы один тип символов")
    password = ''.join(random.choice(characters) for _ in range(length))
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
    return password

try:
    length = int(input("Введите длину пароля: "))
    use_letters = input("Включать буквы? (y/n): ").lower() == 'y'
    use_digits = input("Включать цифры? (y/n): ").lower() == 'y'
    use_symbols = input("Включать специальные символы? (y/n): ").lower() == 'y'
    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"Ваш пароль: {password}")
    print(f"Надежность пароля: {check_strength(password)}")
    print("Пароль сохранён в passwords.txt")
except ValueError as e:
    print(f"Ошибка: {e}")