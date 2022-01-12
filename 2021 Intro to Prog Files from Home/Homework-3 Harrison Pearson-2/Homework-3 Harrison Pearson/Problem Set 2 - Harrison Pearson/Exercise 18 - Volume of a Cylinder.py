# Exercise 18: Volume of a Cylinder
# Takes user input for radius along with height and computes volume
# Output rounded to 1 decimal place

import math

r = input("Please enter the radius of the circular base of the cylinder in m: ")
r = float(r)

h = input("Please enter the height of the cylinder in m: ")
h = float(h)

# CircleArea prsquared
circleArea = math.pi * r**2

# CylinderVolume = circleArea * height
cylinderVolume = circleArea * h

# Result output to 1 decimal place
result = "The volume of the cylinder with the given radius, {rd} meters, along with the given height of {ht} meters, is {vol:.1f}."
print(result.format(rd=r,ht=h,vol=cylinderVolume))
