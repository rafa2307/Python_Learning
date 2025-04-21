"""
def is the key word used to define functions in python.
you can assign default values in the function's arguments
*args lets you pass as many arguments as you want to a fucntion.
"""

"""def my_function ():
    print("Hello world")

def greet(name = "World"):
    print("Hello", name)

def add(a, b = 3):
    return a + b

def add_args(*args):
    result = 0
    for n in args:
        result += n
    return result

my_function()
greet()

number = add(2)

print(number)

print(add_args(1,2,3,4,5,6))"""

def get_color_choice(color):
    try:
        print("Checking if color is available.....")

        company_colors = ["Blue", "Red", "Green", "Pink", "Black"]

        for i in range(len(company_colors)):
            if color == company_colors[i]:
                return color
        else:
            return "The color is not available"
    except Exception as e:
        print(e)



try:
    user_color = input("Enter the crayon color you want: ")

    search_result = get_color_choice(user_color)
    if search_result == user_color:
        print(user_color, " is available for purchase")
    else:
        print(search_result)
    
except Exception as e:
    print(e)

finally:

    user_order = input("How many " + user_color+ " crayons do you want to buy? ")

    order_quantity = int(user_order)

    if order_quantity == 0:
        print("Amount ordered needs to be more than zero")
    else:
        print("Order for " , order_quantity, " has been placed")