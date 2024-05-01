import random

print("Welcome to NumberGuess!")

num1 = random.randrange(0,100)

print("Your random number is generated")
print(num1)

num2 = int(input("Enter your guess between 0 to 99 "))

tracker = 0
while num1 != num2:
    num2 = int(input("Guess again "))
    tracker += 1
else:
    print("Correct guess")
    tracker += 1
    print("You got the correct guess in ", tracker, "attempts")