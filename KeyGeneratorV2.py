import random
import string


def generate_key(length):
    if length < 25 or length > 100:
        raise ValueError("Length must be between 25 and 100 characters.")

    # characters you want to include in the key
    characters = string.ascii_uppercase + string.digits

    # Generate the full code as a string
    key = ''.join(random.choice(characters) for _ in range(length))

    # Format the key into chunks of 5 characters separated by hyphens
    formatted_key = '-'.join(key[i:i + 5] for i in range(0, len(key), 5))

    return formatted_key


# Get user input for the length of the key
length = int(
    input("Enter the desired length of the key (between 25 and 100): "))
try:
    key = generate_key(length)
    print("Generated Key:", key)
except ValueError as e:
    print(e)
