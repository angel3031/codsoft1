import random
import string

print("Welcome to the Password Generator!")

# Ask the user how long they want the password to be
try:
    length = int(input("How long should your password be? "))

    if length < 4:
        print("Oops! Please enter a number 4 or higher for a stronger password.")
    else:
        # Combine letters, numbers, and symbols
        characters = string.ascii_letters + string.digits + string.punctuation

        # Randomly choose characters from the combined list
        password = ''.join(random.choice(characters) for _ in range(length))

        print("\nHere is your strong password:")
        print(password)
except ValueError:
    print("Please enter a valid number.")
