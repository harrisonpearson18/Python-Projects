# Write a Python program to check whether a number is negative, positive or zero.

inputA = float(input("Please enter a number: "))

def numberCheck(input):
    if(input > 0):
        print(input,"is a positive number.")
        return None
    if(input == 0):
        print(input,"is zero.")
        return None
    else:
        print(input,"is a negative number.")
        return None

numberCheck(inputA)