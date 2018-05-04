'''Write a program that asks the user how many Fibonacci numbers to generate
and then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.'''

print("Hey, you! Another game ahead.")


def gen_fib():
    number = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if number == 0:
        fib = []
    elif number == 1:
        fib = [1]
    elif number == 2:
        fib = [1, 1]
    elif number > 2:
        fib = [1, 1]
        while i < (number - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1

    return fib


print(gen_fib())
