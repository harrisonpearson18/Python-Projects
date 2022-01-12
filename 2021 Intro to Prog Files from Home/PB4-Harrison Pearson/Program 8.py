# Write a Python program to input any alphabet and check whether it is vowel or consonant.

inputA = str(input("Please enter a letter to check if it is a vowel or a consonant: "))

def vowelCheck(input):
    input = input.lower()
    if(input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u'):
        print(input,"is a vowel or consonant.")
        return None
    else:
        print(input,"is not a vowel or consonant.")
        return None

vowelCheck(inputA)
