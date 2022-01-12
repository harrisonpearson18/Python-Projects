# Exercise 6 - Sound Levels

def soundreader(input):
    if(input == 40 or input < 40):
        print("A quiet room has a dB level of 40.")
    if(input == 70):
        print("An alarm clock has a dB level of 70.")
    if(input == 106):
        print("A gas lawnmower has a dB level of 106.")
    if(input == 130 or input > 130):
        print("A jackhammer has a dB level of 130.")
    if(input > 40 and input < 70):
        print(input,"is between a quiet room dB of 40 and an alarm clock dB of 70.")
    if(input > 70 and input < 106):
        print(input,"is between an alarm clock dB of 70 and a gas lawnmower dB of 106.")
    if(input > 106 and input < 130):
        print(input,"is between a gas lawnmower dB of 106 and a jackhammer dB of 130.")

dB = int(input("Please enter a dB level: "))

soundreader(dB)
