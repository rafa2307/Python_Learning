s = 'python'
print(f'{s.title()}') # the title function turns the first letter of the string into Uppercase.

n1 = 1
n2 = 2

print(f'{n1} + {n2} = {n1 + n2}') # this prints the addition 1 + 2 = 3.

pi = 3.14159265

print(f'py = {pi:.2f}') # :.2f prints 3.14 because :.2f only prints up to the first 2 decimals of pi

print(f'n1 = {n1:010d}') # this will add 9 zeros infront of n1

print(f'{s.replace("p", "P")}') # replace will replace the first argument with the second argument in the string that is calling the function.

print(f'{s.replace("p", "P")}\n'\
      f'It\' {s}')  # This prints a multi line statement



