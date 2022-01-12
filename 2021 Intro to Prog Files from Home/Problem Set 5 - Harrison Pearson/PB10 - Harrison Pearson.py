# Faces on Money

def facemoney(input):
    if(input == 1):
        print("The face on the",input,"bill is George Washington.")
    if(input == 2):
        print("The face on the", input, "bill is Thomas Jefferson.")
    if(input == 5):
        print("The face on the", input, "bill is Abraham Lincoln.")
    if(input == 10):
        print("The face on the", input, "bill is Alexander Hamilton.")
    if(input == 20):
        print("The face on the", input, "bill is Andrew Jackson.")
    if(input == 50):
        print("The face on the", input, "bill is Ulysses S. Grant.")
    if(input == 100):
        print("The face on the", input, "bill is Benjamin Franklin.")
    else:
        print("No such note exists.")

money = int(input("Please enter a value of a US banknote: "))
facemoney(money)
