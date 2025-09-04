# password_gen.py
import random
import string
import re
import pyperclip

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

def is_unique(password):
    """Check if password is unique in passwords.txt."""
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.read().splitlines()
        return password not in passwords
    except FileNotFoundError:
        return True

def generate_password(length, use_letters=True, use_digits=False, use_symbols=False):
    """Generate a random password with specified length and character types."""
    if length <= 0:
        raise ValueError("Length must be positive")
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # Include lowercase and uppercase letters
    if use_digits:
        characters += string.digits  # Include digits 0-9
    if use_symbols:
        characters += string.punctuation  # Include special characters
    if not characters:
        raise ValueError("At least one character type must be selected")
    attempts = 0
    max_attempts = 100
    while attempts < max_attempts:
        password = ''.join(random.choice(characters) for _ in range(length))
        if is_unique(password):
            with open("passwords.txt", "a") as f:
                f.write(password + "\n")  # Save password to file
            return password
        attempts += 1
    raise ValueError("Could not generate a unique password")

def show_history():
    """Show last 5 passwords from passwords.txt."""
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()[-5:]  # Get last 5 lines
        if passwords:
            print("Last 5 passwords:")
            for i, pwd in enumerate(passwords, 1):
                print(f"{i}. {pwd.strip()} (Strength: {check_strength(pwd.strip())})")
        else:
            print("No passwords in history")
    except FileNotFoundError:
        print("No passwords in history")

def clear_history():
    """Clear passwords.txt."""
    with open("passwords.txt", "w") as f:
        f.write("")  # Clear file content
    print("Password history cleared")

try:
    action = input("Choose action (generate/history/clear): ").lower()
    if action == "generate":
        length = int(input("Enter password length: "))
        count = int(input("Enter number of passwords: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include special characters? (y/n): ").lower() == 'y'
        last_password = ""
        for i in range(count):
            password = generate_password(length, use_letters, use_digits, use_symbols)
            last_password = password
            print(f"Password {i+1}: {password} (Strength: {check_strength(password)})")
        pyperclip.copy(last_password)  # Copy last generated password to clipboard
        print("Last password copied to clipboard")
        print("Passwords saved to passwords.txt")
    elif action == "history":
        show_history()
    elif action == "clear":
        clear_history()
    else:
        print("Invalid action")
except ValueError as e:
    print(f"Error: {e}")