'''
Lesson - 18 Lambda functions
lambda functions
sort(key =)
'''

# labda functions are used when you need a quick function that does not require to be formally defined like the functions that use the def keyword.
add = lambda x: x + 1

print(add(3))

add_numbers = lambda x, y: x + y
print(add_numbers(4,5))

letters = ['yyyy', 'zzz', 'aaaaa', 'xxxxxx', 'wwwwww']
print(letters)
letters.sort(key = lambda x: len(x))
print(letters)

def add_one(n):
    return lambda x: x + n

number = add_one(20)
print(number(5))