import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissor"]



while True:
    user_input = input("Type Rock/Paper or Scissor to continue or 'Q' to quit ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    pick_index = random.randrange(0,3)
    computer_pick = options[pick_index]
    print("Computer picked " + computer_pick)

    if(user_input == "rock" and computer_pick == "scissor"):
        print("You won!")
        user_score += 1
    elif(user_input == "paper" and computer_pick == "rock"):
        print("You won!")
        user_score += 1
    elif(user_input == "scissor" and computer_pick == "paper"):
        print("You won!")
        user_score += 1
    elif(user_input == computer_pick):
        print("Both choose the same. It's a draw!")
    else:
        print("Computer won!")
        computer_score += 1
    
print("You won", user_score, "times")
print("Computer won", computer_score, "times")
