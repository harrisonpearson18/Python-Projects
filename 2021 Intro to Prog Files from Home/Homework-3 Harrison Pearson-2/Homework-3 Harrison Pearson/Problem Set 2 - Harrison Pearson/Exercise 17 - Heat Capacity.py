# Exercise 17: Heat Capacity

# amt of energy required to inc the temp of 1 gram of material by 1 C is the materials heat capacity

# The total amt of energy required to raise m grams of a material by deltaT degrees C can be computed using q = mCdeltaT

# Reads mass of some water, and temperature change from user input (m and deltaT)
# Output the total amount of energy that must be added or removed to achieve desired temp change

# User input for milli litres of water + caste
import math
massWater = input("How many milli-litres of water is being heated / cooled: ")
mass = float(massWater)

# User input for temperature change
deltaT = input("What is the desired change in temperature (C): ")
deltaT = float(deltaT)

C = 4.186
# Energy equation using q = m * C * deltaT
energyQ = mass * C * deltaT
print("The total energy to achieve this temperature change is",energyQ,"Joules.")

# Cost of energy
energyTotal = energyQ * 2.77778*math.e-7
costTotal = energyTotal * 8.9 / 100
costMsg = "The total cost for the energy is ${Q:.2f}."
print(costMsg.format(Q = costTotal))
