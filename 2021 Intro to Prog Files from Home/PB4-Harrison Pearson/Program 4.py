# Write a Python program to check whether a number is divisible by 5 and 11 or not.

inputA = int(input("Please enter a number to check whether divisible by 5 and 11: "))

def divideCheck(input):
    if(input % 5 == 0) and (input % 11 == 0):
        print(input,"is divisible by both 5 and 11.")
        return None
    else:
        print(input,"is not divisible by both 5 and 11.")
        return None

divideCheck(inputA)