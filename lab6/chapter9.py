# Problem 1
def prob_1():
    for i in range(10):
        print("*", end=" ")

# Problem 2
def prob_2():
    for i in range(10):
        print("*", end=" ")
    print()
    for i in range(5):
        print("*", end=" ")
    print()
    for i in range(20):
        print("*", end=" ")
    print()

# Problem 3
def prob_3():
    for i in range(10):
        print()
        for j in range(10):
            print("* ", end="")

# Problem 4
def prob_4():
    for i in range(10):
        print()
        for j in range(5):
            print("* ", end="")

# Problem 5
def prob_5():
    for i in range(5): 
        print() 
        for j in range(20): 
            print("* ", end="")  
        
# Problem 6
def prob_6():
    for i in range(10):
        print()
        for j in range(10):
            print(i, end=" ")

# Problem 7
def prob_7():
    for i in range(10):
        print()
        for j in range(10):
            print(i, end=" ")

# Problem 8
def prob_8():
    for i in range(10):
        print()
        for j in range(i+1):
            print(j, end=" ")

# Problem 9
def prob_9():
    for i in range(10):
        print() 
        for n in range(i): 
            print(" ", end=" ") 
        for j in range(10-i): 
            print(j, end=" ") 

# Problem 10
def prob_10():
    for i in range(10):
        print()
        for row in range(10):
            if i*row < 10:
                print(" ", end=" ")
            else:
                print(" ", end="")
            print(i*row, end=" ")

# Problem 11
def prob_11():
    for i in range(10):
        print()
        for n in range(10-i):
            print(" ", end=" ")
        for row in range(1,1+i):
            print(row, end=" ")
        for j in range(i-1,0,-1):
            print(j, end=" ")

# Problem 12
def prob_12():
    for i in range(10):
        print()
        for n in range(10-i):
            print(" ", end=" ")
        for row in range(1,1+i):
            print(row, end=" ")
        for j in range(i-1,0,-1):
            print(j, end=" ")
    for i in range(10):
        print()
        for n in range(i): 
            print(" ", end=" ") 
        for j in range(9-i): 
            print(j+1, end=" ")

# Problem 13
def prob_13():
    for i in range(10):
        print()
        for n in range(10-i):
            print(" ", end=" ")
        for row in range(1,1+i):
            print(row, end=" ")
        for j in range(i-1,0,-1):
            print(j, end=" ")
    for i in range(10):
        print()
        for n in range(i+2): 
            print(" ", end=" ") 
        for j in range(1, 9-i): 
            print(j, end=" ")
        for j in range(7-i, 0, -1):
            print(j, end=" ")


prob_1()
prob_2()
prob_3()
prob_4()
prob_5()
prob_6()
prob_7()
prob_8()
prob_9()
prob_10()
prob_11()
prob_12()
prob_13()
    