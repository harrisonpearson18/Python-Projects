# Exercise 14: Height Units
# Takes users height in feet then inches
# Computes and displays the equivalent height in ft to centimeters

print("This program will ask for your height, prompting for feet first, then the remaining inches.")
feet = input("Please enter your height starting with feet: ")
inches = input("Now enter the remaining inches: ")
feet = int(feet)
inches = int(inches)

feetToCM = feet * 30.48
inchesToCM = inches * 2.54
totalCM = feetToCM + inchesToCM

output = "Your height of {foot}'{inch}'' is equivalent to {CM} centimeters."
print(output.format(foot = feet, inch = inches, CM = totalCM))
