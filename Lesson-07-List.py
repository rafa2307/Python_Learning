'''
Lists can hold different datatypes
Lists use indeces to access elements in the list
functions to operate on a list: append, insert, pop, remove, reverse, sort, copy, extend and clear
Lists can grow dynamically
'''

first_list = [0, 1, 0.9, True, "String", []]

print(first_list)
print(type(first_list))

print(first_list[0], first_list[-6])

print(first_list[5], first_list[-1])

print(first_list[0:4])

numbers = [10, 11, 12]

print(numbers)

numbers.append(13) # append adds an element to the list at the end.

print(numbers)

numbers.insert(1, 14) # insert lets you specify where in the list you want to add the new element and then shifts all the other elements to the right.

print(numbers)

numbers.pop(0) # pop lets you remove an element from the list in a specific index or if you don't speify the index, it pops the last element.

print(numbers)

numbers.remove(11) # the removes the specific element

print(numbers)

numbers.reverse() # reverses the list

print(numbers)

numbers.sort() # sorts the list

print(numbers)

n = numbers.copy() # creates a shallow copy of the numbers list. Since the numbers list is made of numbers, the list is immutable.

print(n)

numbers.extend(n) # Adds multiple elements to the lost. unlike append which only adds 1

print(numbers)

numbers.clear() # clear will erase the contents of the numbers list

print(numbers, n)