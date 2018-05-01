'''Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)'''

print("Greetings friend! Lets play a little game.")
number = int(input("Give me a random number: "))
x = range(1, number + 1)
a = []

for i in x:
    if number % i == 0:
        a.append(i)
#   print(a)

while a == [1, number]:
    print("Your number is Prime!")
    break
else:
    print("Your number is not Prime!")
