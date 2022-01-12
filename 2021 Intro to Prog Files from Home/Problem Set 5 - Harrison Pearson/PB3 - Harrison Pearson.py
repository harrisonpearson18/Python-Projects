# Exercise 3: Vowel or Consonant

def vowelorcons(input):
    input = input.lower()
    if(input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u'):
        print(input,"is a vowel.")
        return None
    elif(input == 'y'):
        print(input,"is sometimes a vowel and a consonant.")
        return None
    else:
        print(input,"is a consonant.")
        return None
letter = input("Please enter a letter to check for vowel or consonant: ")

vowelorcons(letter)
