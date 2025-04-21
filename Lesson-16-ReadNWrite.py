"""
In this lesson i learned how to read and write files
learned to use the open() function
learned best practices for opening a file
learned how to add a line to a file by using the a command of the open() function
"""

import os

file = open('Lesson-01-String.py')

content = file.read()

print(content)

file.close()

# best practice for opening files

with open('Lesson-02-Variable.py', 'r') as file:
    content = file.read()
    print(content)

with open('output.txt', 'w') as file:
    file.write('First line\n')
    file.write('Second line')

with open('output.txt', 'r') as file:
    content = file.read()
    print(content)

with open('output.txt', 'a') as file:
    file.write(' Second line')

with open('output.txt', 'r') as file:
    print(file.read())
    
os.remove('output.txt')
