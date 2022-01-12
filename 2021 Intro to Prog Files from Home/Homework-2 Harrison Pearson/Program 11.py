#BMI Calculator, takes user's mass(Kg) and height(m)
userMass = input("Please enter your mass in Kg: ")
userHeight = input("Please enter your height in meters: ")
userMass = float(userMass)
userHeight = float(userHeight)
bmiResult = userMass / userHeight**2
print("The result for your BMI is",bmiResult, "kg/m2")