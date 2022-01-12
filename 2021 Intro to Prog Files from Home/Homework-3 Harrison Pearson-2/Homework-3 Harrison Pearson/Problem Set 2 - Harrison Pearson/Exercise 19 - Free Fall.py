# Exercise 19: Free Fall
# Determines how quickly an object is traveling when it hits the ground with vF = v^2i + 2ad
# User inputs height of which object is dropped

import math

h = input("Please enter the height of which the object is dropped in meters: ")
h = float(h)

a = 9.8
vI = 0

vF = vI+2*a*h
vF = math.sqrt(vF)
print(vF)
