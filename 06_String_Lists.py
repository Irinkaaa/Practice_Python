'''Ask the user for a string and print out whether this string is a palindrome or not.
   A palindrome is a string that reads the same forwards and backwards.)'''

print("Lets play another game.")
word = (input("Type in any word you like: "))

if str(word) == str(word[::-1]):
    print("Hey, your word is palindrome!")
else:
    print("Hey, your word is not palindrome!")
