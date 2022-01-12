# Exercise 10: Arithmetic Function
import math
def doArithmetic(intA,intB):
    sum = intB + intA
    print("The sum is",sum)
    diff = intA - intB
    print("The difference is",diff)
    product = intA * intB
    print("The product is",product)
    quot = intA / intB
    print("The quotient is",quot)
    remain = intA % intB
    print("The remainder is",remain)
    result = math.log10(intA)
    print("The result of log10 of a is",result)
    result2 = intA ** intB
    print("The result of a ^ by B is",result2)
    return None

integerA = int(input("Please enter an integer for A: "))
integerB = int(input("Please enter an integer for B: "))
doArithmetic(integerA,integerB)
