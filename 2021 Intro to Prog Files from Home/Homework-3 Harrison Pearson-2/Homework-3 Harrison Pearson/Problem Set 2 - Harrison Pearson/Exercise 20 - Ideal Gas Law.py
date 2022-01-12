# Exercise 20: Ideal gas Law
# PV = nRT
# R = 8.314
# V = 12
# P = 20,000,000
# T = 20 C

p = float(input("Please enter the pressure: "))

v = float(input("Please enter the volume: "))

tempInC = float(input("Please entr the temperature in C: "))
tempInK = 20 * 273.15
constR = 8.314

# n is amount of gas in moles
n = (p*v)/(constR*tempInK)

print('The value of gas in moles is: ', n)
