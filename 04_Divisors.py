'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
   (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is
   a divisor of 26 because 26 / 13 has no remainder.)'''

print("Lets play a game where I tell you all devisors of your number.")
num = int(input("Give me a random number: "))
x = range(1, num)
a = []

for i in x:
    if num % i == 0:
        a.append(i)
print(a)
print("You are welcome!")
