# The Hangman program randomly selects a secret word from a list of secret words. 
# The random module will provide this ability, so line 1 in program imports it.
# The Game: Here, a random word (a fruit name) is picked up from our collection 
# and the player gets limited chances to win the game.
# When a letter in that word is guessed correctly, that letter position 
# in the word is made visible. In this way, all letters of the word are to be 
# guessed before all the chances are over. 
# For convenience, we have given length of word + 2 chances. For example, 
# word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

import random

def choose_fruit():
    fruit_names = ["apple", "banana", "orange", "grape", "kiwi", "mango", "strawberry", "pineapple", "watermelon", "peach"]
    return random.choice(fruit_names)

# function for displaying the word

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def main():
    print("Welcome to the Hangman Game!")
    name = input("Enter your name: ").capitalize()
    print(f"Hello, {name}! Let's start the game.")
    
    word_to_guess = choose_fruit().lower() #lower() is used so that the uppercase in the starting doesn't effect
    guessed_letters = []
    turns = len(word_to_guess) + 2

    while turns > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue
        
        if guess in word_to_guess:
            guessed_letters.append(guess)
            print("Good guess!")
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! You guessed the word correctly.", word_to_guess)
                break #when the word gets completed the program should break even if there's turn left
        else:
            print("Incorrect guess.")
            turns -= 1
            print(f"You have {turns} turns left.")

    if turns == 0:
        print("Sorry, you've run out of turns. The word was:", word_to_guess)

if __name__ == "__main__":
    main()
