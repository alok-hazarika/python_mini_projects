# Write a  Python program to create a person class. Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.
from datetime import date


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

person_1 = Person("Alok", "India", date(1990, 7, 31))
person_2 = Person("Angela", "UK", date(1982, 3, 21))
person_3 = Person("Newborn", "USA", date(2024, 5, 13))
person_4 = Person("Baby", "Italy", date(2024, 2, 13))

print(person_1.calculate_age())
print(person_2.calculate_age())
print(person_3.calculate_age())
print(person_4.calculate_age())