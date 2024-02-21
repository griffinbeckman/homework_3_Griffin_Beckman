#Question 7: Vowels
def vowels(x):
    z = 0
    for i in x:
        if i == "a":
            z += 1
        elif i == "e":
            z += 1
        elif i == "i":
            z += 1
        elif i == "o":
            z += 1
        elif i == "u":
            z += 1
    print(z)