weight = float(input("Enter the weight in kilograms: "))
height = float(input("Enter the height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <=24.9:
    category = "Normal weight"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {bmi}, and you are classified as {category}.")