count = 0

while count < 10:
    print(count)
    count += 1 # You need to increment count by 1 or else you'll have an infinate while loop
else:
    print('Count equals 10')

count = 0

while True:
    print(count)
    count += 1
    if count == 10:
        break
else:
    print('Unuable')

count = 0
while count < 10:
    count += 1
    if count == 5:
        continue # prevents the code after this to execute
    print(count)