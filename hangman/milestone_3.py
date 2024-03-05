"""
Good job so far!
But your code probably doesn't look great.
It's hard to tell which lines do what.


Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.


The check_guess function will take the guessed letter as an argument and check if the letter is in the word.


Step 1:
Define a function called check_guess. pass in the guess as a parameter for the function.
Write the code for the following steps in the body of this function.


Step 2:
Convert the guess into lower case.


Step 3:
Move the code that you wrote to check if the guess is in the word into this function block.


The ask_for_input function.


Step 1:
Define a function called ask_for_input.


Step 2:
Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.


Step 3:
Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.


Step 4:
Outside the function, call the ask_for_input function to test your code.



"""


import random

word_list = ["Banana", "Grapes", "Dates", "Mango", "Watermelon"]


word = random.choice(word_list)
word = word.lower()
print(word, "Random word")

def check_guess(guess):
    guess = guess.lower()
    print(f"here  {guess}")

    if guess in word:
        print(f"Good guess, {guess} is in the word")
    else:
        print(f"{guess} is not in the word, try again")


def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

ask_for_input()

