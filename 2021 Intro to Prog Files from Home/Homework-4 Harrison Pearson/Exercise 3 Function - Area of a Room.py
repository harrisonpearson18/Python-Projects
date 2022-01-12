# Exercise 3: Area of a Room - Function form

def areaOfRoom(input1,input2):
    area = input1 * input2
    print("The area is: ",area)
    return None

length = input('Please enter the length of the room: ')
length = float(length)
width = float(input('Please enter the width of the room: '))

areaOfRoom(length,width)

