import re

password = input("Enter your password: ")

strength = "Weak"

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
    strength = "Strong"
elif len(password) >= 6:
    strength = "Medium"

print("Password Strength:", strength)