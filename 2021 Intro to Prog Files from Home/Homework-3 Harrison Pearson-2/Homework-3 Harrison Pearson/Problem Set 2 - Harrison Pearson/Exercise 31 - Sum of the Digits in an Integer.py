# Exercise 31: Sum of the Digits in an Integer
# Input is 3141
# Pull each digit out for 3 + 1 + 4 + 1 = 9

integer = input("Please enter a four digit integer: ")
integer = int(integer)

numberFour = integer // 1000

numberThree = (integer%1000) // 100

numberTwo = ((integer%1000)%100) // 10

numberOne = (((integer%1000)%100)%10) // 1

sumTotal = numberFour + numberThree + numberTwo + numberOne
print(numberFour,"+",numberThree,"+",numberTwo,"+",numberOne,"=",sumTotal)

