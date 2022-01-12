# Exercise 7: Sum of the first n positive ints function

def sumOfN(input1):
    sum = input1*(input1 + 1)/2
    print("The sum of all integers to",input1,"is",sum)
    return None
n = int(input("Please enter a positive integer: "))
sumOfN(n)
