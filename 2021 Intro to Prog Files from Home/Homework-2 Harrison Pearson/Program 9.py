#Takes a keyboard input of the number of copies purchased
#Finds total cost with a given 40% discount
#Factors shipping costs of 3$ for first copy and 75 cents for each after

copiesPurchased = input("Please enter how many copies are being purchased in this order: ")
copiesPurchased = int(copiesPurchased)
#Total book cost
totalBook = (copiesPurchased * 24.95) * 0.6
#Total shipping cost
totalShip = ((copiesPurchased - 1)*.75) + 3
#Book + Shipping totalCost
totalCost = totalBook + totalShip
print("The total wholesale cost for an order of",copiesPurchased,"copies is $",totalCost,".")