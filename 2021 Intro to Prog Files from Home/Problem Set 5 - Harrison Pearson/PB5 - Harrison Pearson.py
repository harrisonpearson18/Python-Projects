# Month Name to Number of Days

def daycounter(monthinput):

    if (monthinput == 'January'):
        print("There are 31 days in January.")
    if(monthinput == 'February'):
        print("There are 28 or 29 days in February.")
    if(monthinput == 'March'):
        print("There are 31 days in March.")
    if(monthinput == 'April'):
        print("There are 30 days in April.")
    if(monthinput == 'May'):
        print("There are 31 days in May.")
    if(monthinput == 'June'):
        print("There are 30 days in June.")
    if(monthinput == 'July'):
        print("There are 31 days in July.")
    if(monthinput == 'August'):
        print("There are 31 days in August.")
    if(monthinput == 'September'):
        print("There are 30 days in September.")
    if(monthinput == 'October'):
        print("There are 31 days in October.")
    if(monthinput == 'November'):
        print("There are 30 days in November.")
    if(monthinput == 'December'):
        print("There are 31 days in December.")

input = input("Please enter a month of the year: ")

daycounter(input)
