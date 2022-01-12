# Takes user input for positive integer n
# Displays the sum of all of the integers from 1 to n

n = input("Please enter a positive integer: ")
n = int(n)
sum = n*(n+1)/2
sum = int(sum)
print("The sum of all the integers, 1 to",n,", is",sum, ".")
