'''Write a program (function!) that takes a list and returns a new list that contains all the elements
   of the first list minus all the duplicates.
Extras:
    Write two different functions to do this - one using a loop and constructing a list, and another using sets.'''

a = [1, 1, 4, 6, 4, 10, 11, 10, 15, 23, 21, 22, 25]


#   Solution using a for loop
def gen_list(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


print("Random list one generated " + str(a))
print(gen_list(a))


#   Solution using sets
def gen_second_list(a):
    return list(set(a))

print(gen_second_list(a))
