# Exercise 6: Tax or Tip Function

def TaxandTip(input1):
    taxOutput = input1 * 0.04
    tipOutput = input1 * 0.18
    taxMsg = "The total tax for the meal is ${tax:.2f}."
    print(taxMsg.format(tax = taxOutput))
    tipMsg = "The total tip for the meal is ${tip:.2f}."
    print(tipMsg.format(tip = tipOutput))
    totalMeal = input1 + taxOutput + tipOutput
    totalMsg = "The total for the meal with tax and tip is ${total:.2f}."
    print(totalMsg.format(total = totalMeal))

mealCost = float(input("Please enter the cost of the meal ordered: "))

TaxandTip(mealCost)
