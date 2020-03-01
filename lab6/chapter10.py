print(type(3))

x = 3
print("x =", x, "and is of type:", type(x))

x = 3.14159265
print("x =", x, "and is of type:", type(x))

x = "Hi there"
print("x =", x, "and is of type:", type(x))

x = True
print("x =", x, "and is of type:", type(x))

x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))

x = [2, 3, 4, 5]
print("x =", x, "and is of type:", type(x))

x = [1, 2]
print(x[0])

print(x)
x[0] = 22
print(x)

x = (1, 2)
print(x)

# x[0] = 22 throws an error
# print(x)

my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)

my_list = [[2, 3], [4, 3], [6, 7]]
for item in my_list:
    print(item)

my_list = [101, 20, 10, 50, 60]
for index in range(len(my_list)):
    print(my_list[index])

for index, value in enumerate(my_list):
    print(index, value)

my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)

# Create an empty list
my_list = []

for i in range(5):
    user_input = input( "Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    print(my_list)

# Create an array with 100 zeros.
my_list = [0] * 100

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0


# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[index]

print(list_total)

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

for item in my_list:
    # Add each item
    list_total += item

# Print the result
print(list_total)

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop from 0 up to the number of elements in the array:
for index in range(len(my_list)):
    # Modify the element by doubling it
    my_list[index] = my_list[index] * 2

print(my_list)

my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

for item in my_list:
    item = item * 2

print(my_list)

x = "This is a sample string"

print("x=", x)

print("x[0]=", x[0])
print("x[1]=", x[1])
print("x[-1]=", x[-1])
print("x[:6]=", x[:6])
print("x[6:]=", x[6:])
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

for character in "This is a test.":
    print(character)

# Exercise
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
months_list = [i for i in range(1, 13)]
n = int(input("Enter a month number: "))

for num in months_list:
    if int(n) == num:
        index_start = num * 3 - 3
        index_end = num * 3
        print(months[index_start:index_end])

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=" ")

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(ord(c), end=" ")

plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")

plain_text = "This is a test. ABC abc"
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)

x = {}
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

print(x["fred"])