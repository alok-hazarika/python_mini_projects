import random


print("Welcome to the number guessing game!")
random_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if choice == "easy":
    attempts = 10
elif choice == "hard":
    attempts = 5

while attempts > 0:
    print("You have", attempts, "attempts to guess the number")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        if attempts == 1:
            print("You got it wrong! The answer is", random_number)
        else:
            print("Too high.\nGuess Again")
    elif guess < random_number:
        if attempts == 1:
            print("You got it wrong! The answer is", random_number)
        else:
            print("Too low.\nGuess Again")
    else:
        print("You got it! The answer is", guess)
        break
    attempts -= 1
