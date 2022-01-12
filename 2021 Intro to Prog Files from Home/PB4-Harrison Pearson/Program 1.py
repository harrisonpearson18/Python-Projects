# Write a Python program to find maximum between two numbers.

inputA = int(input("Please enter an integer: "))

inputB = int(input("Please enter an integer: "))

def maxNumber(intA,intB):
    if(intA > intB):
        print(intA,"is the largest number.")
        return None
    else:
        print(intB,"is the largest number.")
        return None

maxNumber(inputA,inputB)