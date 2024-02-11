import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            continue
        password = generate_password(length)
        print("Generated password:", password)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
