# Exercise 7: Name that Triangle

side1 = int(input("Please enter the value of a side of the triangle: "))
side2 = int(input("Please enter the value of a side of the triangle: "))
side3 = int(input("Please enter the value of a side of the triangle: "))

def trianglecheck(in1,in2,in3):
    if (in1 == in2 and in2 == in3):
        print("The given triangle is equilateral.")
    if(in1 == in2 and in2 != in3) or (in2 == in3 and in2 != in1) or (in1 == in3 and in1 != in2):
        print("The given triangle is isosceles.")
    if(in1 != in2 and in2 != in3 and in1 != in3):
        print("The given triangle is scalene.")

trianglecheck(side1,side2,side3)

