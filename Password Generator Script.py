import random
import string


def generate_pwd(min_length, numbers = True, special_chars = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    reached_quota = False
    has_num = False
    has_special = False

    while not reached_quota or len(pwd) < min_length:
        add_char = random.choice(characters)
        pwd += add_char

        if add_char in digits:
            has_num = True
        elif add_char in special:
            has_special = True

        reached_quota = True
        if numbers:
            reached_quota = has_num
        if special_chars:
            reached_quota = reached_quota and has_special

    return pwd


min_length = int(input("Enter minimum character length: "))
has_num = input("Include numbers (y/n): ").lower() == "y"
has_special = input("Include special characters (y/n): ").lower() == "y"
pwd = generate_pwd(min_length, has_num, has_special)
print("Successfully generated password:", pwd)