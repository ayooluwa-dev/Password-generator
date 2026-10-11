import secrets

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all_characters = letters + numbers + symbols

while True:
    answer = input("How many characters should the password have? ")
    if answer.isdigit() and int(answer) >= 8:
        password_length = int(answer)
        break
    print("Please enter a whole number of 8 or more.")

password = ""

for i in range(password_length):
    password += secrets.choice(all_characters)

print("Generated Password:", password)
