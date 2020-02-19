import random


def print_intro():
    """ Prints the instructions """

    print("Welcome to Camel!")
    print()
    print("""In your desperation, you have stolen a camel to make your way across 
the great Mobi desert.""")
    print("""The locals want their camel back and are chasing you down! Survive
our desert trek and out run the locals.""")


def main():
    """ The Main program. """

    print_intro()

    done = False

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    locals_traveled = -20
    starting_drinks = random.randint(3, 6)
    drinks_in_canteen = starting_drinks

    while not done:
        print("""

        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.

        """)
        user_choice = input("Your choice? ")

        if user_choice.upper() == "Q":
            done = True
        elif user_choice.upper() == "E":
            print("Miles traveled: ", miles_traveled)
            print("Drinks in canteen: ", drinks_in_canteen)
            print("The locals are ", miles_traveled - locals_traveled, " miles behind you")

        elif user_choice.upper() == "D":
            camel_tiredness = 0
            locals_traveled += random.randint(7, 14)
            print("Your camel is happy.")

        elif user_choice.upper() == "C":
            distance = random.randint(10, 18)
            miles_traveled += distance
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            locals_traveled += random.randint(7, 14)
            print("You traveled ", distance, " miles.")
        
        elif user_choice.upper() == "B":
            distance = random.randint(5, 12)
            miles_traveled += distance
            thirst += 1
            camel_tiredness += 1
            locals_traveled += random.randint(7, 14)
            print("You traveled ", distance, " miles.")
        
        elif user_choice.upper() == "A":
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                thirst = 0
                locals_traveled += random.randint(3, 7)
                print("Thirst quenched.")
            else:
                print("You have no drinks left!")
        
        if thirst > 4 and thirst < 7:
            print("You are thirsty.")
        elif thirst > 6:
            print("You died of thirst!")
            done = True
        
        
        if camel_tiredness > 5 and camel_tiredness < 9 and not done:
            print("Your camel is getting tired.")
        elif camel_tiredness > 8:
            print("You worked your camel to death.")
            print("""While walking, you're clumsy self tripped fell, \
breaking your frail neck. :(""")
            done = True

        if locals_traveled >= miles_traveled and not done:
            print("The locals have caught you and beheaded you. :(")
            done = True
        elif (miles_traveled - locals_traveled) < 15 and not done:
            print("The locals are getting close!")
        
        if miles_traveled >= 200 and not done:
            print("You have escaped! You win!")
            done = True
        
        if random.random() < 0.10 and not done:
            print("You have found an oasis!")
            drinks_in_canteen = starting_drinks
            thirst = 0
            camel_tiredness = 0


if __name__ == "__main__":
    main()


    
