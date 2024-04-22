# importing 
import random
import time
import os

# premium version to generate keys quicker or otherwise | create a system that you can buy to unlock [premium : version]
premium = True 

# characters lower, upper, and digits
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"

# characters to make it true to enable certain stuff you want to generate your key
upper, lower, nums, syms = True, True, True, False

# all is the key, but to generate you have to input the chars + amount
all = ""

# checking if its true or false and += to
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

# starting point for both vars here are at 0 since there is inputs | length has to be below 60 | amount can be anything ex. Amount = 100000
length = 0
amount = 0

# checking if its true or false if the user has premium
if premium == False:
    give_amount = int(input("Generate key(s) amount: "))
    give_length = int(input("Characters length amount: "))

if premium == True:
    give_amount = int(input("Premium | Generate key(s) amount: "))
    give_length = int(input("Premium | Characters length amount: "))

# setting the amount and length to its input amount
amount = give_amount
length = give_length

# sets this amount received to amount for counter
amount_received = amount

# looping to generate the keys for the input amount
for x in range(amount):
    password = "".join(random.sample(all, length))
    amount_received = amount_received - 1
    print(f"generating... | keys left: {amount_received + 1}")
    # checks if the premium is true or false to make the wait time less or high between premiums
    if premium == True:
        time.sleep(0.03)
        print(f"{password} | succesfully generated! | PREMIUM VERSION")
    if premium == False:
        time.sleep(3)
        print(f"{password} | succesfully generated! | upgrade with premium to generate keys quicker!ß")

    # checks if the amount is 0 then it will print
    if amount_received == 0:
        print("Finished generating tokens/key(s)!")
        time.sleep(180)
        os.system('clear')
