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

# Here i will try to write code that uses everything that i have learned until now.
    
try:
    list = []
    print('Please enter 5 numbers. Enter one number at a time.')
    for i in range(5):
        num = input('Please enter a number: ')
        list.append(int(num))
    count = 0
    while count < 5:
        print(list[count])
        count += 1
    for item in range(len(list)):
        if list[item] == 3:
            print(list[item]/0)
        print(list[item]/5)
except Exception as e:
    print(e)