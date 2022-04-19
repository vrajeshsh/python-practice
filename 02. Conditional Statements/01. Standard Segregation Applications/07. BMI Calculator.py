'''To calculate BMI based on weight and height of the user'''

print("To calculate BMI based on weight and height of the user: ")
weight = float(input("Enter the weight (in Kgs): "))
height = float(input("Enter the height (in metres): "))

bmi = weight/(height**2)

if bmi < 15:
	category = "Starvation"
elif bmi < 18.5:
	category = "Underweight"
elif bmi < 25:
	category = "Normal"
elif bmi < 30:
	category = "Overweight"
elif bmi < 40:
	category = "Obese"
else:
	category = "Morbidly Obese"

print("\nBMI Category: ",category)

if bmi < 18.5 or bmi >= 25:
	ideal_weight = 21.75*(height**2)
	print("\nIdeal Weight: ", round(ideal_weight,2),"Kgs")

