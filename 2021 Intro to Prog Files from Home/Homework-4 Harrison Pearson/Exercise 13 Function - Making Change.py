# Exercise 13: Making Change function

def makeChange(input1):
    toonies = input1 // 200
    remainder = input1 % 200
    print("Toonies:",toonies)
    loonies = remainder // 100
    remainder = remainder % 100
    print("Loonies:",loonies)
    quarters = remainder // 25
    remainder = remainder % 25
    print("Quarters:",quarters)
    dimes = remainder // 10
    remainder = remainder % 10
    print("Dimes:",dimes)
    nickles = remainder // 5
    remainder = remainder % 5
    print("Nickles:",nickles)
    pennies = remainder // 1
    print("Pennies:",pennies)
    return None

change = int(input("Please enter an integer of cents to be converted to change: "))

makeChange(change)