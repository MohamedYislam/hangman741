

import random

favourite_fruits = ["Banana", "Grapes", "Dates", "Mango", "Watermelon"]

word_list = favourite_fruits
print(word_list)

word = random.choice(word_list)
print(word, "Random word")




guess = input("Enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Invalid input")