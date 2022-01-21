# Write a Python program to create a word guessing game kind of like Hangman. Program should do the following operations:

# a) Program chooses random word from list of words.

# b) Limited guesses before game ends.

# c) Addresses repeats when guessing.

# d) Displays progress after each guess

import random

words = ['american']
random_word = random.choice(words)
count = 0
attempt_list = []

while True:
    guess = str(input('Guess a letter: ')).lower()

    if guess not in attempt_list:
        if guess in random_word:
            print('Its in the word')
        else:
            count += 1
            print('Not in word, attemps: {}'.format(count))

            if count >= 5:
                print('\nYou have reached max attempts')
                print('Sorry, but hangman died! You lose')
                break
    else:
        print('You already guessed {}. Try again'.format(guess))
        print(set(attempt_list))

    attempt_list.append(guess)
