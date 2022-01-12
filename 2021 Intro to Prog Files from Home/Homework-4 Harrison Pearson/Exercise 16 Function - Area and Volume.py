# Exercise 16: Area and Volume function
import math
def areaAndVolume(radius):
    areaOfCircle = math.pi*radius**2
    print("The area of a circle with the given radius is:",areaOfCircle)
    volumeOfSphere = 4/3*math.pi*radius**3
    print("The volume of a sphere with the given radius is:",volumeOfSphere)
    return None
radiusInput = float(input("Please enter a radius to compute with: "))
areaAndVolume(radiusInput)
