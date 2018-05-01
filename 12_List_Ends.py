'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
   and makes a new list of only the first and last elements of the given list. For practice,
   write this code inside a function.'''

a = [5, 10, 15, 20, 25]
b = []

#   Solution without function
for i in a:
    if i == a[0]:
        b.append(i)
    if i == a[-1]:
        b.append(i)
print(b)


#   Solution with function
def select(x):
    return x[0], x[-1]


print(select(a))
