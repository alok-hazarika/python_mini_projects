boy = input("Enter your name: ")
girl = input("Enter your lover's name: ")

list1 = list(boy.replace(" ","").lower())
list2 = list(girl.replace(" ","").lower())

final_list = list1 + list2

score1 = 0
score2 = 0


for el in final_list:
    if el == "t":
        score1 += 1
    elif el == "r":
        score1 += 1
    elif el == "u":
        score1 += 1
    elif el == "e":
        score1 += 1


for el in final_list:
    if el == "l":
        score2 += 1
    elif el == "o":
        score2 += 1
    elif el == "v":
        score2 += 1
    elif el == "e":
        score2 += 1


love_score = str(score1) + str(score2)

love_score = int(love_score)
        
if 10 > love_score > 90:
    print("Your score is", love_score, "you go like coke and mentos")
elif 40 < love_score < 50:
    print("Your score is", love_score, " you go alright together")
else:
    print("Your score is", love_score)
