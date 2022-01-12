# Exercise 11: Fuel Efficiency
# Takes user input for American fuel efficiency (Miles per Gallon)
# Converts user input to Liters / 100 KM
# 1 Miles per Gallon = 235.215 Liters per 100 Kilometers

milesPerGallon = input("Please enter your vehicle's Miles per Gallon: ")
MPG = float(milesPerGallon)
LKM = MPG * 235.215
print("For the value " + milesPerGallon + " miles per gallon is equal to",LKM,"Liters per 100 Kilometers.")