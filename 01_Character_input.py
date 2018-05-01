'''Create a program that asks the user to enter their name and their age.
   Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
   Add on to the previous program by asking the user for another number
   and printing out that many copies of the previous message.
   Print out that many copies of the previous message on separate lines.'''

print("Hello there! Let me tell you a secret.")
name = str(input("Give me your name: "))
print("Hey, " + name)


age = int(input("Tell me how old are you: "))
current_year = 2018

number = int(input("Pick a number between 1 and 10: "))


def calculate_year(year):
    born_year = current_year - year
    future_year = born_year + 100
    return future_year


hundred_year = str(calculate_year(age))

print(("Hey, %s you will be 100 years old in " % name + hundred_year + "! HAHAHA" + '\n') * number)
