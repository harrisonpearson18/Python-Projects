# Exercise 15: Distance Units
# Takes user input of a number of feet
# Converts user input to equivalent distances in inches, yards, and miles

userFeet = input("Please enter the number of feet you wish to convert: ")
feet = float(userFeet)

# feet -> inches
inches = feet * 12
print(userFeet + " is equivalent to",inches,"inches.")

# feet -> yards
yards = feet * 0.333333
print(userFeet + " is equivalent to",yards,"yards.")

# feet -> miles
miles = feet * 0.000189394
print(userFeet + " is equivalent to",miles,"miles.")