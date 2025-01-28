import secrets
import string

# ⚠️ this doesnt actually print xbox / psn codes its just to generate random 5x5 / 4x4 patterns randomly.

def generate_xbox_code():
    # Define allowed characters for Xbox code (excluding A, E, I, O, U, L, S, 0, 1, 5)
    characters = ''.join([char for char in string.ascii_uppercase + string.digits if char not in "AEIOULS015"])
    
    # Generate a secure random Xbox code (25 characters long)
    key = ''.join(secrets.choice(characters) for _ in range(25))
    
    # Format the Xbox key into a 5x5 pattern (XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)
    formatted_key = '-'.join(key[i:i+5] for i in range(0, 25, 5))

    return formatted_key

def generate_psn_code():
    # Define allowed characters for PSN code (excluding A, E, I, O, U, L, S, 0, 1, 5)
    characters = ''.join([char for char in string.ascii_uppercase + string.digits if char not in "AEIOULS015"])
    
    # Generate a secure random PSN code (12 characters long)
    key = ''.join(secrets.choice(characters) for _ in range(12))
    
    # Format the PSN code into a 4x4 pattern (XXXX-XXXX-XXXX)
    formatted_key = '-'.join(key[i:i+4] for i in range(0, 12, 4))

    return formatted_key

# Decision prompt
code_type = input("Do you want to generate an Xbox code or a PSN code? (Enter 'Xbox' or 'PSN'): ").strip().lower()

# Get user input for the number of codes to generate
amount = int(input("Enter the number of codes you want to generate: "))

# Generate the specified number of codes based on the user's choice
if code_type == 'xbox':
    keys = [generate_xbox_code() for _ in range(amount)]
    print("\nGenerated Xbox Codes:")
    for key in keys:
        print(key)
elif code_type == 'psn':
    keys = [generate_psn_code() for _ in range(amount)]
    print("\nGenerated PSN Codes:")
    for key in keys:
        print(key)
else:
    print("Invalid input. Please enter 'Xbox' or 'PSN'.")


# CREDITS:  made by icyMods on github
