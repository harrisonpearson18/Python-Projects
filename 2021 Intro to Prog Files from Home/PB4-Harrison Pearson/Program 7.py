# Write a Python program to check whether a character is alphabet or not.

inputA = (input("Please enter a character of the alphabet: "))

def letterCheck(input):

    if(input.isalpha()):
        print(input,"is a letter.")
        return None
    else:
        print(input,"is not a letter.")
        return None


letterCheck(inputA)