'''Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extra:
    Randomly generate two lists to test this'''

#   Solution with random lists
import random
list1 = random.sample(range(16), 10)
list2 = random.sample(range(26), 8)
list3 = []


def generate(a, b):
    for i in a:
        if i in b:
            list3.append(i)


generate(list1, list2)

print("First random list is: " + str(list1))
print("Second random list is: " + str(list2))
print("Here is a new list of common items: " + str(list3))


#   One line solution
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = [i for i in a if i in b]
print(result)
