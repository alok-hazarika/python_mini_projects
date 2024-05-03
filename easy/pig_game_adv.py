import random

players = 0

def roll():
    val = random.randint(1,6)
    return val
    
while True:
    user_input = input("Enter number of players : ")
    if user_input.isdigit():
        user_input = int(user_input)
        if 2<= user_input <=4:
            players = user_input
            break
        else:
            print("Enter between 2 & 4")
    else:
        print("Enter a valid option")

player_scores = [0 for _ in range(players)]

max_permitted_score = 50

while max(player_scores)<max_permitted_score: 
    for player_idx in range(players):
        print("Turn of player number ", player_idx + 1)
        print("Your total score is ", player_scores[player_idx])
        current_score = 0
        while True:
            choice = input("Do you want to roll? type 'y' to roll " )
            if choice.lower() == "y":
                value = roll()
                if(value == 1):
                    print("\nYou rolled a 1! Scored 0! Turn done!\n")
                    current_score = 0
                    break
                else:
                    print("You rolled a ", value)
                    current_score += value
                    print("Your score", current_score)
            else:
                break
        player_scores[player_idx] += current_score

max_score = max(player_scores)
win_idx = player_scores.index(max_score)

print("player number ", win_idx +1, " won with a score of", max_score )



    

