# Exercise 14: Height Units function

def heightSwap(input1,input2):
    feettoinches = input1 * 12
    totalinches = feettoinches + input2
    totalCM = totalinches * 2.54
    print("Your height in centimeters is:",totalCM)
    return None

feet = int(input("Please enter your height, first the foot value: "))
inches = int(input("Now please enter the remaining inches: "))
heightSwap(feet,inches)
