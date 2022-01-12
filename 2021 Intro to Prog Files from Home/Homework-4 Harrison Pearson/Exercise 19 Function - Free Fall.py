# Exercise 19: Free Fall function
import math
def freeFall(distance):
    a = 9.8
    vI = 0
    result = math.sqrt(vI+2*a*distance)
    print("The final speed of the object before hitting the ground from the given distance is: ",result,"m/s.")
    return None
distanceInput = float(input("Please enter the distance of which the object is dropped from: "))
freeFall(distanceInput)
