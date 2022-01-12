# Exercise 4: Area of a Field
# This program will take user inputs for a farmer's field
# Given a length and width in feet from user, it will calculate the area in acres
# 43,560 square ft = 1 acre

print("In order to determine the acres on a farmers field please provide the following information.")
length = input("Please enter the length of the field in feet: ")
width = input("Please enter the width of the field in feet: ")
length = float(length)
width = float(width)
areaInfeet = length * width
areaInacres = areaInfeet / 43560
print("This area of the field in acres is",areaInacres,"acres.")