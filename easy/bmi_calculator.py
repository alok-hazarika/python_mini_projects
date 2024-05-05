#BMI calculator using user input


height = float(input("Enter your height in meter\n"))

weight = float(input("Enter your weight in kg\n"))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Your BMI is low. You seem to be underweight. Your BMI is", bmi)
elif 18.5 <= bmi <= 24.9:
    print("Your BMI is good. You seem to have a healthy weight. Your BMI is", bmi)
elif 24.9< bmi <= 29.9:
    print("Your BMI is high. You seem to be overweight. Your BMI is", bmi)
else:
    print("Your BMI is too high. You seem to be obese. Your BMI is", bmi)