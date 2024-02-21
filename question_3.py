#Question 3: Check Leap Year
def leap_year(x):
    if (x % 4 == 0):
        if (x % 100 != 0):
            print(x)
        elif (x % 400 == 0):
            print(x)
        else:
            return