'''
In this lesson i learned about the match statement. It's similar to the switch statement from java.
'''

command = input('Choose a greeting: ')

match command:
    case '1':
        print('Hi')
    case '2':
        print('Hello')
    case _:
        print('Invalid Choice')

item = ['Hello', 2, 3.12]

match item:
    case int(x) if x > 0:
        print('Item is a positive number', x)
    case str(x):
        print('Item is a string', x)
    case list(x):
        print('Item is a list', x)