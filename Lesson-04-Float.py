'''
We learned about floats, int fucntion and float function.
'''

f1 = 3.6

print(type(f1))

f2 = 3.

print(type(f2))

n1 = 10

f3 = n1 / n1 # / return a float
print(type(f3), f3)

n2 = n1 // n1 # // returns an integer. This operator is used for integer division
print(type(n2), n2)

print(type(n1 * f3), n1 * f3) # All arythmetic operation with a float results in a float.

n1 = float(n1)

print(type(n1), n1)

n1 = int(n1)

print(type(n1), n1)