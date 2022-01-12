# Exercise 15: Distance Units Function

def distUnits(input):
    inches = input * 12
    print("The value in inches is:",inches)
    yards = input * 0.33333
    print("The value in yards is:",yards)
    miles = input * 0.000189394
    print("The value in miles is:",miles)
    return None

feet = int(input("Please enter a value in feet you wish to convert: "))
distUnits(feet)