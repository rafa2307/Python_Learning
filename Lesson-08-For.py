"""
In this lesson i learned how use a for loop, range function, nested for loops and the for else loop.
i also learned about the len function. which gives you the length of a list or string.
"""

numbers = [0, 1, 2, 3]

print(numbers)

for n in numbers: # this for loop wil print all the numbers in the numbers array.
    print(n)

for i in range(10): # this for loop will print number from 1 to 10 exluding 10.
    print(i)

my_name = 'Red'
print(my_name[0])

print(len(my_name)) # the len function gives you the

for i in range(len(my_name)):
    print(my_name[i])

matrix = []

for i in range(1, 3):
    for j in range(4):
        pair = [i, j]
        matrix.append(pair)
        print("i = " , i, "j = " , j)

print(matrix)

print(len(matrix))

for i in range(50): # for else code block executes whatever is in the else statement as long as the loop finishes
    if i > 7:
        break
    print(i)
else:
    print("The loop is done")