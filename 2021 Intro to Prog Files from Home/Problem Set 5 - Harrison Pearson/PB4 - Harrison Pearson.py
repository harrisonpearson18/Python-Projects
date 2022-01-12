# Exercise 4: Name that shape

def shapenamer(input):
    if(input < 3):
        print("The provided sides isn't a shape.")
    elif(input >= 3 and input <= 10):
        if(input == 3):
            print("The provided sides makes a triangle.")
        if(input == 4):
            print("The provided sides makes a square or rectangle.")
        if(input == 5):
            print("The provided sides makes a pentagon")
        if(input == 6):
            print("The provided sides makes a hexagon.")
        if(input == 7):
            print("The provided sides makes a heptagon.")
        if(input == 8):
            print("The provided sides makes an octagon.")
        if(input == 9):
            print("The provided sides makes a nonagon.")
        if(input == 10):
            print("The provided sides makes a decagon.")
    if(input > 10):
        print("The shape with the provided sides is incompatible for this program.")

shape = int(input("Please enter the number of sides of a shape: "))

shapenamer(shape)
