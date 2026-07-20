import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_characters = letters + numbers + symbols

password_length = int(input("How many characters should the password have? "))

password = ""

for i in range(password_length):
    password += random.choice(all_characters)

print("Generated Password:", password)