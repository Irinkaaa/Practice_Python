'''Ask the user for a number.
   Depending on whether the number is even or odd, print out an appropriate message to the user.
Extras:
   If the number is a multiple of 4, print out a different message.
   Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
   If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''

print("Lets play a simple game?")
num = int(input("Give me a random number: "))
check = int(input("Now give me a random number to check if it evenly divides by this one: "))

if num % 2 == 0 and num % 4 == 0:
    print("Hey, your first number is Even and a muptiple of 4!")
elif num % 2 == 0:
    print("Hey, your first number is Even!")
elif num % 2 != 0:
    print("Hey, your first number is Odd!")

if num % check == 0:
    print("And your numbers evenly devide each other!")
else:
    print("But your numbers do not evenly devide each other!")
