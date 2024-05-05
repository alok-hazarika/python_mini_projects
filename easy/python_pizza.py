print("Welcome to Python Pizza")
size = input("Which size of pizza would you like to order? S, M or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

base_price = 0
pepp_price = 0
cheese_price = 0

if size == "s":
    base_price = 15
elif size == "m":
    base_price = 20
elif size == "l":
    base_price = 25
else:
    print("Invalid selection! Try again")

if add_pepperoni == "y":
    if size == "s":
        pepp_price = 2
    elif size == "m" or size == "l":
        pepp_price = 3
    else:
        print("Invalid selection! Try again")
elif add_pepperoni == "n":
    print("Okay!")
else:
    print("Invalid selection! Try again")

if extra_cheese == "y":
    cheese_price = 1
elif extra_cheese == "n":
    print("Okay, no extra cheese")
else:
    print("Invalid selection! Try again")

total = base_price + pepp_price + cheese_price

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is ${total}")