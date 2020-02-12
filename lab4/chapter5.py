def print_hello():
    """ This is a comment that describes the function. """
    print("Hello!")

def print_goodbye():
    print("Bye!")
    

def main():
    """ This is my main program function """
    print_hello()
    print_goodbye()

def print_number(my_number):
    print(my_number)

print_number(55)
print_number(25)
print_number(8)

def add_number(a, b):
    print(a, b)

add_number(11, 7)

# Add two numbers and return the results
def sum_two_numbers(a, b):
    result = a + b
    return result

# This doesn't do much, because we don't capture the result
sum_two_numbers(22, 15)

# Capture the function's result into a variable by putting "my_result =" 
# in from of it. (Use whatever variable name best describes the data, 
# don't blindly use 'my_result' for everything.)
my_result = sum_two_numbers(22, 15)

# Now that I captured the result, print it.
print(my_result)

def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

six_pack_volume = volume_cylinder(2.5, 5) * 6

# Function that prints the result.
def sum_print(a, b):
    result = a + b
    print(result)

# Function that returns the result. 
def sum_return(a, b):
    result = a + b
    return result

# This prints the sum of 4+4
sum_print(4, 4)

# This does not
sum_return(4, 4)

# This will not set x1 to the sum.
# It actually gets a value of 'None'.
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum.
# and print it properly
x2 = sum_return(4, 4)
print("x2 =", x1)

def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result

x = 45
y = 56

average = calculate_average(x, y)
print(average)

def volume_cylinder(radius, height):
    """ Returns volume of a cylinder given radius, height """
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

# Define a simple function that sets x equal to 22
x = 44

def f():
    x += 22
    print(x)

f()
print(x)

# Define a simple function that prints x
def f(x):
    x += 1
    print(x)

x = 10
f(x)
print(x)

# Example 1
def a():
    print("A")

def b():
    print("B")

def c():
    print("C")

a()

# Example 2
def a():
    b()
    print("A")

def b():
    c()
    print("B")

def c():
    print("C")

a()

# Example 3
def a():
    print("A")
    b()

def b():
    print("B")
    c()

def c():
    print("C")

a()

# Example 4
def a():
    print("A start")
    b()
    print("A end")

def b():
    print("B start")
    c()
    print("B end")

def c():
    print("C start and end")

a()

# Example 5
def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)

def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)

def c(x):
    print("C start and end, x =", x)

a(5)

# Example 6
def a(x):
    x = x + 1

x = 3
a(x)

print(x)

# Example 7
def a(x):
    x = x + 1
    return x

x = 3
a(x)

print(x)

# Example 8
def a(x):
    x = x + 1
    return x 

x = 3
x = a(x)

print(x)

# Example 9
def x(x, y):
    x = x + 1
    y = y + 1
    print(x, y)

x = 10
y = 20
a(y, x)

# Example 10
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y 

x = 10
y = 20
z = a(x, y)

print(z)

# Example 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10
y = 20 
z = a(x, y)

print(z)

# Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10 
y = 20
x2, y2 = a(x, y) 
print(x2)
print(y2)

# Example 13
def a(my_data):
    print("functon a, my_data = ", my_data)
    my_data = 20
    print("function a, my_data = ", my_data)

my_data = 10

print("global scope, my_data =", my_data)
a(my_data)
print("global scope, my_data =", my_data)

# Example 14
def a(my_list):
    print("function a, list =  ", my_list)
    my_list = [10, 20, 30]
    print("function a, list =  ", my_list)

my_list = [5, 2, 4]

print("global scope, list =", my_list)
a(my_list)
print("global scope, list =", my_list)

# Example 15
# New concept!
# Covered in more detail in a later chapter
def a(my_list):
    print("function a, list = ", my_list)
    my_list[0] = 1000
    print("function a, list = ", my_list)

my_list = [5, 2, 4]

print("global scope, list = ", my_list)
a(my_list)
print("global scope, list = ", my_list)

# Only run the main function if we are running this file. Don't run it if 
# we are importing this file.
if __name__ == "__main__":
    main()


