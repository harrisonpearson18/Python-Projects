# Write a Python program to check whether a number is even or odd.

inputA = int(input("Please enter a number to check if it is even or odd: "))

def evenOrOdd(input):
    if(input % 2 == 0):
        print(input,"is even.")
        return None
    else:
        print(input,"is odd.")
        return None

evenOrOdd(inputA)
