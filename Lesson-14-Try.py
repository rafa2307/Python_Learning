try:
    print(10/0)
except Exception as e:
    print(e)
    #pass
print('Program ended')

try:
    i = input('Enter a number: ')
    i = int(i)
    print(i)
    print(10/i)
except ValueError:
    print(i, 'is not a number')
except ZeroDivisionError:
    print('i can\'t be zero')
else:
    print('I prints if there aren\'t errors')
finally:
    print('I print always')