# Write a Python program to find maximum between three numbers.

inputA = int(input("Please enter an integer: "))

inputB = int(input("Please enter an integer: "))

inputC = int(input("Please enter an integer: "))

def maxNumber(intA,intB,intC):

    if(intA > intB) and (intA > intC):
        print(intA,"is the largest number.")
        return None
    if(intB > intA) and (intB > intC):
        print(intB,"is the largest number.")
        return None
    if(intC > intA) and (intC > intB):
        print(intC,"is the largest number.")
        return None

maxNumber(inputA,inputB,inputC)
