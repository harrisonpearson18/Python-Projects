# Write a Python program to check whether a year is leap year or not.

yearInput = int(input("Please enter a year to check if it is a leap year: "))

def leapYear(input):
    if (input % 4 == 0):
        if (input % 100 == 0):
            if (input % 400 == 0):
                print(input,"is a leap year.")
            else:
                print(input,"is not a leap year.")
        else:
            print(input,"is a leap year.")
    else:
        print(input,"is not a leap year.")

leapYear(yearInput)
