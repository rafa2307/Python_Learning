'''
This file is for reviewing what i learned in the List lesson.
'''

# How to create a list

myList = [1,3.4,5,"Hello", False]

# This for loop will print out the index of each of the elements in the list
for i in range(len(myList)):
    print(i)

# This for loop prints out the values in the list and the types of each value
for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

# Below are some of the functions for a list.
    
# append(n) will add an element to the end of the list
myList.append(True)

for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

# insert(x, y) x represents the index and y the value you want to insert in the list

myList.insert(1, 12) # we inserted 12 in index 1 and this lead to the list growing by one element. 
                     # insert lest us add a new element tot he list at a specific index

for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

# pop() or pop(index). pop() removes the last element in the list while pop(index) removes an element from the list at a specific index

myList.pop()

for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

myList.pop(2)

for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

# remove(value): remove() will remove the first instance of a value in a list
myList.append(12) # this will add 12 to the end of myList
myList.remove(12) # this will remove the first instance of 12 from myList

for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

# reverse(): this method reverses the a list.

myList.reverse()

for i in range(len(myList)):
    print("Value: ", myList[i], " And", " Type: ", type(myList[i]))

# sort() this method sorts a list in ascednig order by default
# sort() only works for lists that have the same types. In the case of myList, it threw an error as there are multiple types in this list.
    
try:
    myList.sort()
except Exception as e:
    print(e)

myList2 = [1, 4, 33 ,22, 55, 77, 5 ,8 ,19 ,99 ,30, 10]

print("Original myList2: ", myList2)

myList2.sort()

print("Sorted myList2")

for i in myList2:
    print(i)

# copy(): this method creates a shallow copy of the original list. This means that if you make changes to the copy list, the original list will not be affected.

numbers = myList2.copy()

print("original numbers list: ", numbers)

numbers.append(101) # this does not affect myList2

numbers.insert(4, 66) # this does not affect myList2

print("myList2: ", myList2)

print("numbers: ", numbers)

# extend(n): this method allows you to add lists, tuples, sets or a string to the end of a list.

strings = ["Hello", "World", "Ruby", "Is", "My", "Beautiful", "Girlfriend"]

numbers.extend(strings)

print("numbers list after extending it with the strings list:", numbers)

# clears(): this method clears the whole list of any value

numbers.clear()

print("numbers list after calling the clear method:", numbers)

