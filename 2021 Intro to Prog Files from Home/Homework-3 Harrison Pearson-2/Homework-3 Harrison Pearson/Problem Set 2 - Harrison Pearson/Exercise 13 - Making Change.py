# Exercise 13: Making Change
# Takes user input of number of cents as an integer
# Pennies - 0.01, Nickles - 0.05, Dimes - 0.10, Quarters - 0.25, Loonies - 1$, Toonies - 2$

cents = input("Please enter the change due as an integer: ")
cents = int(cents)

toonies = cents // 200

remaining = cents % 200
loonies = remaining // 100

remaining = remaining % 100
quarters = remaining // 25

remaining = remaining % 25
dimes = remaining // 10

remaining = remaining % 10
nickles = remaining // 5

remaining = remaining % 5
pennies = remaining // 1

print("Toonies =",toonies)

print("Loonies =",loonies)

print("Quarters =",quarters)

print("Dimes =",dimes)

print("Nickles =",nickles)

print("Pennies =",pennies)


