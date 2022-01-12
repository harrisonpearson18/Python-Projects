# Exercise 11: Date to Holiday Name

def datetoholiday(in1,in2):
    if(in1 == 'January' and in2 == 1):
        print("The holiday on the given date is New year's day.")
    if(in1 == 'July' and in2 == 1):
        print("The holiday on the given date is Canada day.")
    if(in1 == 'December' and in2 == 25):
        print("The holiday on the given date is Christmas day.")

month = input("Please enter a month of the year: ")
day = int(input("Please enter a day of the month you provided: "))

datetoholiday(month,day)
