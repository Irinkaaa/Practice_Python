'''Generate a random number between 1 and 9 (including 1 and 9).
  Ask the user to guess the number, then tell them whether they guessed too low,
  too high, or exactly right.
Extras:
   Keep the game going until the user types “exit”
   Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

import random

print("Greetings, friend! Would you like to play a little game?")
ran_num = int(random.randint(1, 10))
guess = 0
count = 0

while guess != ran_num and guess != "exit":
    guess = int(input("Give me a number between 1 and 9, else type 'exit' : "))
    if guess == "exit":
        print("Game over!")
        break
        count += 1
    if guess > ran_num:
        print("Your number is too high :( !")
        count += 1
    elif guess < ran_num:
        print("Your number is too low :( !")
        count += 1
    else:
        print("Great Job! You guessed it!")
        count += 1
        print("And it only took you " + str(count) + " tries!")
        break
