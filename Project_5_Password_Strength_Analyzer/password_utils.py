import re
import random
import string
from cryptography.fernet import Fernet
import os
import base64


def get_encryption_key():
    key_file = 'secret.key'
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return key

cipher_suite = Fernet(get_encryption_key())


def analyze_password_strength(password):
    score =0
    suggestions=[]

    if len(password)>=8:
        score+=1
    else:
        suggestions.append("Make it at least 8 characters long.")
    

    if re.search(r"[A-Z]",password):
        score+=1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    
    if re.search(r"[a-z]",password):
        score+=1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")
    
    if score<=2:
        strength = "Weak"

    elif score == 3 or score ==4:
        strength = "Moderate"

    else:
        strength ="Strong"


    return strength,suggestions

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*(),.?\":{}|<>")

    
    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>"
    remaining_chars = [random.choice(all_characters) for _ in range(remaining_length)]

    
    password_list = list(lowercase + uppercase + digit + special) + remaining_chars
    random.shuffle(password_list)
    return ''.join(password_list)

def save_credentials(username, password):
    encrypted_username = cipher_suite.encrypt(username.encode()).decode()
    encrypted_password = cipher_suite.encrypt(password.encode()).decode()
    
    with open('saved_password.txt', 'a') as f:
        f.write(f"{encrypted_username}:{encrypted_password}\n")

def get_saved_credentials():
    try:
        with open('saved_password.txt', 'r') as f:
            lines = f.readlines()
        
        credentials = []
        for line in lines:
            encrypted_username, encrypted_password = line.strip().split(':')
            username = cipher_suite.decrypt(encrypted_username.encode()).decode()
            password = cipher_suite.decrypt(encrypted_password.encode()).decode()
            credentials.append((username, password))
        return credentials
    except FileNotFoundError:
        return []