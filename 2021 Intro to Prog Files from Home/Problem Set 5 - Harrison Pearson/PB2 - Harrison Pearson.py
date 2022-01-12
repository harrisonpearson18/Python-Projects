# Exercise 2: Dog Years

def dogyears(num):
    dogyeartotal = 0
    if(num>2):
        dogyeartotal += 10.5
        newnum = num-2
        dogyeartotal += newnum * 4
        print("The dog is",dogyeartotal,"years old.")
    elif(num<2) and not (num<0):
        dogyeartotal += num*5.25
        print("The dog is",dogyeartotal,"years old.")
    elif(num<0):
        print("You cannot enter a negative value.")

number = float(input("Please enter the number of human years your dog is: "))

dogyears(number)
