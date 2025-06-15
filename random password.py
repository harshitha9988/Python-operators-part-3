import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    password = random.choice(lower) + random.choice(upper) + random.choice(digits)

    all_chars = lower + upper + digits
    password += ''.join(random.choices(all_chars, k=length-3))

    password_list = list(password)
    random.shuffle(password_list)
    
    return ''.join(password_list)

print("Generated Password:", generate_password())