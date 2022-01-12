# Write a Python program to input any character and check whether it is alphabet, digit or special character.



def inputChecker():
    inputA = input("Please enter any character on the keyboard: ")

    if(inputA.isalpha()):
        print(inputA,"is a letter.")
        return None
    if(inputA.isnumeric()):
        print(inputA,"is a letter.")
    else:
        print(inputA,"is a special character.")

inputChecker()
