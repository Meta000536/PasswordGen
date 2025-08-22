# password_gen.py
import random
import string
import re

def check_strength(password):
    """Check password strength based on length and character types."""
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    return "Strong" if score >= 3 else "Weak" if score <= 1 else "Medium"

def generate_password(length, use_letters=True, use_digits=False, use_symbols=False):
    """Generate a random password with specified length and character types."""
    if length <= 0:
        raise ValueError("Length must be positive")
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("At least one character type must be selected")
    password = ''.join(random.choice(characters) for _ in range(length))
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
    return password

try:
    length = int(input("Введите длину пароля: "))
    count = int(input("Введите количество паролей: "))
    use_letters = input("Включать буквы? (y/n): ").lower() == 'y'
    use_digits = input("Включать цифры? (y/n): ").lower() == 'y'
    use_symbols = input("Включать специальные символы? (y/n): ").lower() == 'y'
    for i in range(count):
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"Пароль {i+1}: {password} (Надежность: {check_strength(password)})")
    print("Пароли сохранены в passwords.txt")
except ValueError as e:
    print(f"Ошибка: {e}")