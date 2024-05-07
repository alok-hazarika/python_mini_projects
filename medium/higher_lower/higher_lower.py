import random
from game_data import data

score = 0
guess = True

##############################
# creating the first person and properties from game_data
##############################
person_A = data[random.randrange(0, len(data))]

contender_A= person_A["name"]
desc_A = person_A["description"]
country_A = person_A["country"]
follower_A = person_A["follower_count"]
question_A = f"{contender_A}, a {desc_A}, from {country_A}"

##############################
# while loop until user gets the answer wrong
##############################

while guess:    
##############################
# creating the second person and properties from game_data
##############################
    pick_idx = random.randrange(0, len(data))
    person_B = data[pick_idx]
    contender_B= person_B["name"]
    desc_B = person_B["description"]
    country_B= person_B["country"]
    follower_B = person_B["follower_count"]
    question_B = f"{contender_B}, a {desc_B}, from {country_B}"

##############################
# checking if both the person is not the same
##############################
    if person_A != person_B:
        print("Compare A: ",question_A)
        print("VS")
        print("Against B: ",question_B)
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        if user_input == "A":
            if person_A["follower_count"] > person_B["follower_count"]:######## if the guess is right
                question_A = question_B
                person_A = person_B
                score += 1
            elif person_A["follower_count"] < person_B["follower_count"]:######## if the guess is wrong
                print("Game Over! Your score is", score)
                guess = False
            else:                                                       ######## for invalid selection
                print("Invalid selection! Game over")
                break

        if user_input == "B":
            if person_A["follower_count"] < person_B["follower_count"]:
                question_A = question_B
                person_A = person_B
                score += 1
            elif person_A["follower_count"] > person_B["follower_count"]:
                print("Game Over! Your score is", score)
                guess = False
            else:
                print("Invalid selection! Game over")
                break
