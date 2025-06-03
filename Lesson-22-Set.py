# sets are mutable, but the data inside a set must be of immutable type such as number, string and tuple

# this is how you create a set.
s = {1,3,2,4,5,5,5}

print(type(s), s)
# This is how you create a empty set
empty = set()

print(type(empty), empty)

# Sets can have different types in them. but each of the type smust be an immutable type.
s1 = {'a', True, 2, 3.14}

print(type(s1), s1)

try:
    print(s[0])
except:
    print("You can't access set values through index")

# this is how you can check if something is in the set
if 1 in s:
    print("1 is present")

# this is how you can iterate through a set
for element in s:
    print(element)

l = [1,2,1,2,1,1,3,3,3]

print(set(l))

# most common methdos for a set

s.add(6)

print(s)
# adding 6 to the set again will result in 6 being ignored and not added since 6 is already in the set.
s.add(6)

print(s)

s.remove(6)

print(s)

# discard is used if you don't know if the element is in the set
s.discard(5)

print(s)

s.pop()
# pop removed the first element in a set.
print("This is s after the pop: ", s)

s2 = s.copy()

print(s2)
# this prints the intersection between the sets
print(s1.intersection(s))
# this prints the union of both sets
print(s1.union(s))
# This prints the difference between the 2 sets.
print(s1.difference(s))
# this clears the set and turns it into an empty set.
s1.clear()

print(s1)