import random
import string

def generated_password(length=12):
    characters = string.ascii_letters +string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password 

#user input
length =int(input("Enter the length of your password:"))

password = generated_password(length)

print("Generated password:", password)
