'''
Dictionaries use a key value pair. To print a single value you need the key paired with the value.
'''

lessons = {'Lesson 01': 'String', 'Lesson 02': 'Variables', 'Lesson 03': 'Integer'}

print(lessons)

print(lessons['Lesson 01'])

print(lessons.keys()) # the keys() fucntion will return only the keys in the dictionary

print(lessons.values()) # the values() fucntion will return only the values in the dictionary

lessons['Lesson 04'] = 'Float' # this is how you add a new key value pair to the end of the dict

print(lessons)

for key in lessons:
    print('Key: ' , key , 'Value: ' , lessons[key])

del lessons['Lesson 04']

for i in range(len(lessons)):
    print(list(lessons.values())[i]) # in this line we're appending all of the values in lessons to the list and then accessing the current list value at i