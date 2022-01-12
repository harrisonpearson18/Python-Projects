# Exercise : 1 Even or Odd

def evenorodd(num):
    if (num % 2 == 0):
        print("The number is even.")
        return None
    else:
        print("The number is odd.")

number = int(input("Please enter an integer: "))

evenorodd(number)
    