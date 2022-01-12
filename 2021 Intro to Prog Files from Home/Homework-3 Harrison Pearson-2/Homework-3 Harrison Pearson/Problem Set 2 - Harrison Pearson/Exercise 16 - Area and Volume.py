# Exercise 16: Area and Volume
# takes radius, r, as input from user
# computes and outputs area of a circle with radius r
# computes and outputs volume of a sphere with radius r

import math
# User inputs radius
radius = input("Please enter a radius for the circle object: ")
r = float(radius)

# Area of a circle pi r^2
circleArea = math.pi*r**2
areaMessage = "The area of a circle with the given radius, {rd}, is {Area:.4f}."
print(areaMessage.format(rd = r, Area = circleArea))

# Volume of a sphere 4/3 pi r^3
sphereVolume = 4/3 * math.pi*r**3
volumeMessage = "The volume of a sphere with the given radius, {rd}, is {Volume:.4f}."
print(volumeMessage.format(rd = r, Volume = sphereVolume))

