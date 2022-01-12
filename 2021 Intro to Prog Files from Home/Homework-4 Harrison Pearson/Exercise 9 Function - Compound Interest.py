# Exercise 9: Compound Interest Function

def compoundInt(deposit1):
    year1 = (deposit1 * 0.04) + deposit1
    year1Msg = "The value after one year is ${value:.2f}."
    print(year1Msg.format(value = year1))
    year2 = (year1 * 0.04) + year1
    year2Msg = "The Value after two years is ${value:.2f}."
    print(year2Msg.format(value = year2))
    year3 = (year2 * 0.04) + year2
    year3Msg = "The valye after three years is ${value:.2f}"
    print(year3Msg.format(value = year3))
deposit = float(input("Please enter the amount being deposited into your savings account: "))

compoundInt(deposit)
