# Exercise 6: Tax and Tip
# Takes user input for cost of meal
# Program computes tax on meal using local rate of 4 percent
# Computes a tip of 18 percent of the meal amount
# Outputs the tax amount. tip amount, and grand total of the meal (tax & tip)

mealPrice = input("Please enter the cost of the meal: ")
mealPrice = float(mealPrice)
mealTax = mealPrice * 0.04
mealTip = mealPrice * 0.18
taxTxt = "The tax for the given meal price is ${price:.2f}."
print(taxTxt.format(price = mealTax))
tipTxt = "The tip for the give meal price is ${price:.2f}."
print(tipTxt.format(price = mealTip))
mealTotal = mealPrice + mealTax + mealTip
totalTxt = "The grand total for the given meal price is ${price:.2f}."
print(totalTxt.format(price = mealTotal))