name=input('What is your name? :')
#here the user is asked to enter first name
print("Good Luck!",name)
# Define a list of words
words=['rainbow','computer','science','programming','python','mathematics','player',
       'condition','reverse','water','board','geeks','solve','gain',
       'apple','zebra','yolo','Damascus']

import random
word = random.choice(words)  # Select a random word
print("Guess the characters:")
guesses = ""  # Stores guessed letters
turns = 12  # Number of attempts
while turns > 0:
    failed = 0  # Track if any letters are missing
    # Display the current word status
    for char in word:
        if char in guesses:
            print(char, end=" ")  # Show guessed letters
        else:
            print("_", end=" ")  # Hide unguessed letters
            failed += 1  # Increase fail count

    print()  # Move to the next line
    # Check if all letters are guessed
    if failed == 0:
        print("You won!")
        print("The word is:", word)
        break

    # Get user input
    guess = input("Guess a character: ").lower()
    # Add guessed character to the guesses string
    guesses += guess
    # Check if the guessed character is in the word
    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print("You have", turns, "more guesses left.")

        if turns == 0:
            print("You lose! The word was:", word)
