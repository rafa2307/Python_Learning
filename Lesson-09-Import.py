import os # this statement lets me interact with OS of my machine.
from random import randint # randint generates a randum integer value. You have to set a range from x to y.
from datetime import datetime as dt # datetime lets you set date. You have to pass arguments to the function in the following order: yy, mm, dd, hour, min, sec
from datetime import timedelta # timedelta adds days to the date in datetime
import math as mt # the math module lets you use different math functions

cwd = os.getcwd() # getcwd() returns the current working directory

print(cwd)

files = os.listdir() # listdir() returns the files inside the current working directory

print(files)

os.system('cls||clear') # by usineg the system() function from the OS module and running this command cls||clear, you can clear what's in the terminal

for i in range(10):
    print(randint(1,10))

print("My random integer: ", randint(1, 20))

time = dt(2022, 6, 1, 2, 4, 20)

print(time)

print(time + timedelta(10))

print(mt.cos(3.14), mt.sin(3.14), mt.tan(3.14))




