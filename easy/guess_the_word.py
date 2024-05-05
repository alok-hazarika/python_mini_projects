# # In this game, there is a list of words present, out of which our 
# # interpreter will choose 1 random word. The user first has to input their 
# # names and then, will be asked to guess any alphabet. If the random word 
# # contains that alphabet, it will be shown as the output(with correct placement) 
# # else the program will ask you to guess another alphabet. The user will be 
# # given 12 turns(which can be changed accordingly) to guess the complete word.



import random

def choose_word():
    words = [
    "Tokyo",
    "Paris",
    "London",
    "Beijing",
    "Rome",
    "Istanbul",
    "Moscow",
    "Dubai",
    "Sydney",
    "Cairo",
    "Mumbai",
    "Seoul",
    "Berlin",
    "Amsterdam",
    "Bangkok",] # List of words
    return random.choice(words)

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
    print("Welcome to the Word Guessing Game!")
    name = input("Enter your name: ").capitalize()
    print(f"Hello, {name}! Let's start the game.")
    
    word_to_guess = choose_word().lower() #lower() is used so that the uppercase in the starting doesn't effect
    guessed_letters = []
    turns = 12

    while turns > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue
        
        if guess in word_to_guess:
            guessed_letters.append(guess)
            print("Good guess!")
            if set(word_to_guess) == set(guessed_letters):
                attempt = 12 - turns
                print(f"Congratulations! You guessed the word correctly. You got only", attempt, "guess wrong")
                break #when the word gets completed the program should break even if there's turn left
        else:
            print("Incorrect guess.")
            turns -= 1
            print(f"You have {turns} turns left.")

    if turns == 0:
        print("Sorry, you've run out of turns. The word was:", word_to_guess)

if __name__ == "__main__":
    main()
