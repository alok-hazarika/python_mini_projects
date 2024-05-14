import random

class Bank:
    def __init__(self, name):
        self.name = name
        self.usernames = []
        self.types = []
        self.ac_numbers = []
        self.ac_balances = []


    def create_account(self, username, type):
        account_number = random.randint(0,5000)
        if username not in self.usernames:
            self.usernames.append(username)
            self.types.append(type)
            self.ac_numbers.append(account_number)
            self.ac_balances.append(0)
            print("User added! username -", username," and account type -", type, "and account number -", account_number)
        else:
            print("User already exists!")
    
    def deposit_money(self, username, amount):
        if username in self.usernames:
            user_idx = self.usernames.index(username)
            self.ac_balances[user_idx] += amount
            print(f"Availabe balance of {username} is {self.ac_balances[user_idx]}")
        else:
            print("User doesn't exist!")
    
    def withdraw_money(self, username, amount):
        if username not in self.usernames:
            print("User doesn't exist!")
        if username in self.usernames:
            user_idx = self.usernames.index(username)
            if amount <= self.ac_balances[user_idx]:
                self.ac_balances[user_idx] -= amount
                print(f"Availabe balance of {username} is {self.ac_balances[user_idx]}")
            else:
                print("Not enough money in the account!")
        




yes_bank = Bank("Yes bank")
yes_bank.create_account("Alok Hazarika", "Savings")
yes_bank.deposit_money("Alok Hazarika", 10000)
yes_bank.deposit_money("Alok Hazarika", 5000)
# yes_bank.withdraw_money("Alok Hazarika", 18000)

axis_bank = Bank("Axis bank")
axis_bank.create_account("Alok Hazarika", "Savings")
