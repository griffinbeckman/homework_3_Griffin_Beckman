#Question 1: Power of a Number
def exponential(x, y):
    z = 1
    while y > 0:
        z = z*x
        y -= 1
    print(z)