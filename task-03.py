import string
import re

def check_length(password):
    if len(password) < 8:
        return 0
    elif len(password) > 8 and len(password) < 16:
        return 1
    elif len(password) > 16:
        return 2

def check_characters(password):
    pattern = r"[A-Z]|[a-z]|[0-9]|[!@#$%^&*()_+-=[]{};':\"|,.<>/\?~€£¥§ªº«»©®™]"
    if re.search(pattern, password):
        return 2
    elif re.search(r"[A-Z]|[a-z]", password):
        return 1
    else:
        return 0

def assess_password_strength(password):
    length_result = check_length(password)
    character_result = check_characters(password)
    return max(length_result, character_result)

def feedback(complexity):
    if complexity == 0:
        print("Your password is too weak. Try adding uppercase letters, numbers, and special characters to make it more secure, and aim for a minimum of 8 characters.")
    elif complexity == 1:
        print("Your password is okay, but it could be stronger. Consider adding 1-2 more characters and including a mix of uppercase letters, numbers, and special characters to make it more secure.")
    elif complexity == 2:
        print("Great job! Your password is strong and secure. Keep up the good work!")
    else:
        print("error")

password = input("password = ")
complexity = assess_password_strength(password)
feedback(complexity)