'''Write a program (using functions!) that asks the user for a long string containing multiple words.
   Print back to the user the same string, except with the words in backwards order.'''


def reverse(a):
    b = a.split()
    c = b[::-1]
    d = " ".join(c)
    print(d)


string = str(input("Enter a long string containing multiple word, please: "))

reverse(string)
