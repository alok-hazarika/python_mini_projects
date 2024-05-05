#Simple tip calculator for group visiting a restaurant
#Total Bill, % of total bill and no. of people in the group are given as inputs
#The program calculates and displays the amount for each person.

print("Welcome to tip calculator")
total = float(input("What was the total bill ? $"))
percent = int(input("How much tip would you like to give? 10, 12 or 15 %? "))
people = int(input("How many people to split the bill?" ))

tip = (total + (total * percent * .01))/people
payable = round(tip, 2)
print(f"Each person should pay: ${payable}")
