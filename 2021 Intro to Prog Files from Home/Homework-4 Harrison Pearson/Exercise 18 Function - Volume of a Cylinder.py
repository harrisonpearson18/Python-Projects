# Exercise 18: Volume of a cylinder function
import math
def volumeOfCyl(radius,height):
    area = math.pi*radius**2
    volume = area*height
    print("The volume of a cylinder with the given parameters is:",volume)
    return None

radiusInput = float(input("Please enter a radius to compute with: "))
heightInput = float(input("Please enter a height to compute with: "))

volumeOfCyl(radiusInput,heightInput)
