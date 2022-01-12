# Exercise 9: Compound Interest
# Takes user input of amount deposited into savings account
# Savings account accrues 4 percent interest per year
# Outputs total amount in savings after 1, 2, and 3 years
# Outputs to be formatted to two decimal places <- will also add $ sign

deposit = input("Please enter the amount to be deposited into your new savings account: ")
deposit = float(deposit)
yearOneInterest = deposit * 0.04
yearOneTotal = deposit + yearOneInterest
yearTwoInterest = yearOneTotal * 0.04
yearTwoTotal = yearOneTotal + yearTwoInterest
yearThreeInterest = yearTwoTotal * 0.04
yearThreeTotal = yearTwoTotal + yearThreeInterest
# Year 1 total output
yearOneTxt = "After one year your savings account will contain ${total:.2f}."
print(yearOneTxt.format(total = yearOneTotal))
# Year 2 total output
yearTwoTxt = "After two years your savings account will contain ${total:.2f}."
print(yearTwoTxt.format(total = yearTwoTotal))
# Year 3 total output
yearThreeTxt = "After three years your total savings account will contain ${total:.2f}."
print(yearThreeTxt.format(total = yearThreeTotal))