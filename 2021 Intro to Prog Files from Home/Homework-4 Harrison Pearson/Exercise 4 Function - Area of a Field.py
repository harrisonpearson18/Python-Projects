# Exercise 4: Area of a field function
# Inputs in feet and output in acres

def areaOfField(input1,input2):
    area = input1*input2
    areaToAcre = area / 43560
    print("The area of the field is",areaToAcre,"acres.")

length = float(input('Please enter the length of the field in feet: '))
width = float(input('Please enter the width of the field in feet: '))

areaOfField(length,width)
