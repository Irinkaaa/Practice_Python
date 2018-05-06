'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
   print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock'''

name1 = input("Player1, what is your name?: ")
name2 = input("Player2, what is your name?: ")


def game():
    r = "rock"
    p = "paper"
    s = "scissors"
    player1 = input(str(name1) + ", pick one: rock, paper, or scissors?: ").lower()
    player2 = input(str(name2) + ", now you pick one: rock, paper, or scissors?: ").lower()
    if player1 == player2:
        print("You are even!")
    elif player1 == r and player2 == p:
        print(str(name2) + ", you WIN!")
    elif player1 == r and player2 == s:
        print(str(name1) + ", you WIN!")
    elif player1 == p and player2 == r:
        print(str(name1) + ", you WIN!")
    elif player1 == p and player2 == s:
        print(str(name2) + ", you WIN!")
    elif player1 == s and player2 == r:
        print(str(name2) + ", you WIN!")
    elif player1 == s and player2 == p:
        print(str(name1) + ", you WIN!")


game()
question = input("Do you want to play again? (yes/no): ").lower()
while question == "yes":
    game()
    question = input("Do you want to play again? (yes/no): ").lower()
