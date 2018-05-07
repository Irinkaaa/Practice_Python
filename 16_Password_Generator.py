'''Write a password generator in Python. Be creative with how you generate passwords
   - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
   The passwords should be random, generating a new password every time the user asks for a new password.
   Include your run-time code in a main method.
Extra:
    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''

import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbols = "!@#$%^&*()?"

strong = upper + lower + symbols + numbers
medium = upper + lower
weak = lower + numbers

lenght = int(input("How long do you want your password to be: "))


def gen_pass(lenght):
    difficulty = input("Do you want your password to be weak, medium or strong: ")
    if difficulty == "strong":
        password = random.sample(strong, lenght)
        for i in password:
            password = "".join(password)
        print(password)
    if difficulty == "medium":
        password = random.sample(medium, lenght)
        for i in password:
            password = "".join(password)
        print(password)
    if difficulty == "weak":
        password = random.sample(weak, lenght)
        for i in password:
            password = "".join(password)
        print(password)


gen_pass(lenght)
