word_list = ["acknowledgement", "apple", "mango", "rabbit"]

import random

choosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")