# Exercise 12: Distance between two points on earth
import math
def showDistance(l1,g1,l2,g2):

    distance = 6371.01 * math.acos(math.sin(l1)*math.sin(l2)+math.cos(l1)*math.cos(l2)*math.cos(g1-g2))
    print("The distance between the two given points is:",distance,"Km.")
    return None

lat1 = math.radians(float(input("Please enter the latitude for point1: ")))
long1 = math.radians(float(input("Please enter the longitude for point1: ")))

long2 = math.radians(float(input("Please enter the longitude for point2: ")))
lat2 = math.radians(float(input("Please enter the latitude for point2: ")))

showDistance(lat1,long1,lat2,long2)
