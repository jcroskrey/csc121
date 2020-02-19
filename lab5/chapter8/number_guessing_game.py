"""
Random Number Guessing Game
"""
import random


def main():
    print("Hï! I'm thinking of a random number between 1 and 100.")

    # Create a secret number
    secret_number = random.randrange(1, 101)

    # Initialize our attempt count, we start with attemp 1.
    user_attempt = 1
    
    # Set user guess to something secret_number can't be, so we
    # can start our while loop.
    user_guess = 0

    win_by_asking = False

    # Loop until user_guess==secret_number, or we run out of attempts.
    while user_guess != secret_number and user_attempt < 8:
        
        # Tell the user what attempt we are on, and get their guess:
        print("-- Attempt", user_attempt)
        user_input_text = input("Guess what number I am thinking of:")
        if user_input_text == "please tell me":
            win_by_asking = True
            print("Fine. Since you asked nicely, we'll let you win.")
            print("The number was " + str(secret_number) + " btw.")
            break
        else:
            user_guess = int(user_input_text)

            # Print if we are too high or low, or we got it.
            if user_guess > secret_number:
                print("Too high.")
            elif user_guess < secret_number:
                print("Too low.")
            else:
                print("You got it!")
                break
        
        # Add to the attemt count
        user_attempt += 1
        # Check to see if the user didn't guess the answer, and ran out of tries
        # Let her know what the number was, so she doesn't spend the rest of
        # life wondering.
    if user_guess != secret_number and win_by_asking == False:
        print("Aw, you ran out of tries. The number was " + str(secret_number) \
        + ".")
    
main()
    
