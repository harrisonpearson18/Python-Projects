# Write a Python program to check whether a character is uppercase or lowercase alphabet.

def checkLetter():
    inputA = input("Please enter a character of the alphabet: ")

    if(inputA.isupper()):
        print(inputA,"is an uppercase letter.")
        return None
    else:
        print(inputA,"is a lowercase letter.")
        return None

checkLetter()
