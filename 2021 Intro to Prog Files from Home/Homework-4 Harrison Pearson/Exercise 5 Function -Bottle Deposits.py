# Exercise 5: Bottle Deposits Function

def bottleReader(input1,input2):
    oneLorL = input1 * 0.10
    morethanL = input2 * 0.25
    total = oneLorL + morethanL
    totalmsg = "Your total refund is ${refund:.2f}."
    print(totalmsg.format(refund = total))

bottle1 = int(input("Please enter the number of bottles one liter or less deposited: "))
bottle2 = int(input("Please enter the number of bottles over one liter deposited: "))

bottleReader(bottle1,bottle2)
