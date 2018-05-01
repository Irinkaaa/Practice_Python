'''Take two lists, say for example these two:
   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
   and write a program that returns a list that contains only the elements that are common
   between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
   Randomly generate two lists to test this
   Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)'''

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

#   Multiple line solution with duplicates :(
for i in a:
    if i in b:
        c.append(i)
print(set(c))

#   One line solution without duplicates (Extra 2)
print(list(set(a).intersection(b)))

#   Solution with random lists (EXtra 1)
d = random.sample(range(25), 7)
e = random.sample(range(35), 9)
f = []

for i in d:
    if i in e:
        f.append(i)

print(f)
