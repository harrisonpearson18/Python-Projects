# Exercise 16: Richter Scale

def magnitudecheck(input):
    if(input < 2):
        print("The earthquake with the given magnitude is considered a Micro earthquake.")
    if(input >= 2 and input < 3):
        print("The earthquake with the given magnitude is considered a Very minor earthquake.")
    if(input >= 3 and input < 4):
        print("The earthquake with the given magnitude is considered a Minor earthquake.")
    if(input >= 4 and input < 5):
        print("The earthquake with the given magnitude is considered a Light earthquake.")
    if(input >= 5 and input < 6):
        print("The earthquake with the given magnitude is considered a Moderate earthquake.")
    if(input >= 6 and input < 7):
        print("The earthquake with the given magnitude is considered a Strong earthquake.")
    if(input >= 7 and input < 8):
        print("The earthquake with the given magnitude is considered a Major earthquake.")
    if(input >= 8 and input < 10):
        print("The earthquake with the given magnitude is considered a Great earthquake.")
    if(input >= 10):
        print("The earthquake with the given magnitude is considered a Meteoric earthquake.")

mag = float(input("Please enter the magnitude of an earthquake to determine its description: "))

magnitudecheck(mag)
