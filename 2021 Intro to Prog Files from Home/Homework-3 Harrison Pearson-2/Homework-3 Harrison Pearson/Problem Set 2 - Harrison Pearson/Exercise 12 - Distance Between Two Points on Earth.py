# Exercise 12: Distance Between Two Points on Earth
# Takes user input for 2 locations of lat and longs
# Variables are f1,g1 and f2,g2
# Given equation distance = 6371.01 x arccos(sin(f1) x sin(f2) + cos(f1) x cos(f2) x cos(g1-g2))
import math

print("This program will determine the distance between two points given by the user.")
# Location 1
f1 = input("Please enter the latitude degrees of point 1: ")
f1 = float(f1)
f1 = math.radians(f1)
g1 = input("Please enter the longitude degrees of point 1: ")
g1 = float(g1)
g1 = math.radians(g1)
# Location 2
f2 = input("Please enter the latitude degrees of point 2: ")
f2 = float(f2)
f2 = math.radians(f2)
g2 = input("Please enter the longitude degrees of point 2: ")
g2 = float(g2)
g2 = math.radians(g2)
# Distance equation
distance = 6371.01 * math.acos(math.sin(f1) * math.sin(f2) + math.cos(f1) * math.cos(f2) * math.cos(g1 - g2))
# Output
print("This distance between the two given points is",distance,"Kilometers.")