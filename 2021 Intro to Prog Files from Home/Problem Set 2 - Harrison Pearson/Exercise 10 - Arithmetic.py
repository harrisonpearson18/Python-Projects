# Exercise 10: Arithmetic
# Takes user input for two integers a and b
# Computes and displays the following
# Sum of a and b
# Difference when b is subtracted from a
# Product of a and b
# Quotient when a is divided by b
# Remainder when a is divided by b
# Result of log10 a
# Result of a^b

import math

a = input("Please enter an integer for variable a: ")
b = input("Please enter an integer for variable b: ")
a = int(a)
b = int(b)
print("")
# sum
sum = a + b
print("The sum of a and b is =",sum)
print("")
# difference a - b
diff = a - b
print("The difference of b subtracted from a is =",diff)
print("")
# product
prod = a * b
print("The product of a and b is =",prod)
print("")
# quotient
quot = a / b
print("The quotient of a divided by b is =",quot)
print("")
# remainder
remain = a % b
print("The remainder when a is divided by b is =",remain)
print("")
# log10a
result = math.log10(a)
print("The result of log10(a) is =",result)
print("")
# a^b
result = a**b
print("The result of a^b is =",result)