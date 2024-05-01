def initialise():
    print("WELCOME TO MASTERQUIZ")
    cont = input("Do you want to continue? Press 'Y'\nor press 'N' to exit ")
    if(cont.lower() == "n"):
        print("Come back when you change your mind")
        quit
    elif(cont.lower() == "y"):
        print("Okay let's play")
        quiz_run()
    else:
        print("Invalid selection")
        initialise()

def quiz_run():
    count = 0
    score = 0
    answer = input("What stands for CPU? ").lower()
    if answer == "central processing unit":
        print("Correct!")
        score += 3
        count += 1
    else:
        print("Incorrect!")
        score -= 1

    answer = input("What stands for GPU? ").lower()
    if answer == "graphics processing unit":
        print("Correct!")
        score += 3
        count += 1
    else:
        print("Incorrect!")
        score -= 1
    
    answer = input("What stands for RAM? ").lower()
    if answer == "random access memory":
        print("Correct!")
        score += 3
        count += 1
    else:
        print("Incorrect!")
        score -= 1

    answer = input("What stands for PSU? ").lower()
    if answer == "power supply unit":
        print("Correct!")
        score += 3
        count += 1
    else:
        print("Incorrect!")
        score -= 1
    
    answer = input("What is the full form of ROM? \n A. Random Only Memory\n B. Read On Memory\n C. Read Only Memory\n D. None of the above\n Type only A, B, C or D ").lower()
    if answer == "c":
        print("Correct")
        score += 3
        count += 1
    else:
        print("Incorrect")
        score -= 1
    percentage = (count/5) * 100
    print("You got ", count,"answers correct out of 5 which is ", percentage,"%")
    print("Your score is :", score)

initialise()