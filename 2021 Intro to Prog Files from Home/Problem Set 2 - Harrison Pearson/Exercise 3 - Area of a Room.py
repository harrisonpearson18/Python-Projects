# Exercise 3: Area of a Room
# Takes user input of length and width, casted to floating numbers to find area in feet

print("This program will calculate the area of a room in feet, given length and width.")
length = input("Please enter the length of the given room in feet: ")
width = input("Please enter the width of the given room in feet: ")
length = float(length)
width = float(width)
area = length * width
print("The area of the given room using the provided length and with is",area,"square feet.")