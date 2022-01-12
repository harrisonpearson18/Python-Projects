# Exercise 5: Bottle Deposits
# Takes user input of number of bottles holding 1 liter or less - $0.10 deposit
# Takes user input of number of bottles holding more than 1 liter - $0.25 deposit
# Takes these inputs and displays the refund given with $ sign and two decimals

print("Bottle Deposit")
print("Bottles holding 1 liter or less refund at $0.10.")
print("Bottles holding more than 1 liter refund at $0.25.")
oneLiterOrLess = input("Please enter the number of bottles being deposited that hold 1 liter or less: ")
moreThanLiter = input("Please enter the number of bottles being deposited that hold more than 1 liter: ")
oneLiter = int(oneLiterOrLess)
moreLiter = int(moreThanLiter)
oneLiterRefund = oneLiter * 0.10
moreLiterRefund = moreLiter * 0.25
totalRefund = oneLiterRefund + moreLiterRefund
message = "Your total refund is ${refund:.2f} dollars."
print(message.format(refund = totalRefund))
