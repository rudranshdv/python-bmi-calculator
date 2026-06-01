print(".....BMI CalCulator.....")

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(meters): "))

BMI = weight/(pow(height,2))

print(f"BMI is {round(BMI,2)}")
