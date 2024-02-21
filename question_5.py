#Question 5: Rotating Digits
def rotate_digits(n):
    z = (n % 10)*(10**(len(str(n))-1)) + (n // 10)
    print(z)