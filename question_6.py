#Question 6: Minimum and Maximum but with Loops
def min_for_loop(x):
    z = x[0]
    for i in x:
        if i < z:
            z = i
    print(z)

def max_for_loop(x):
    z = x[0]
    for i in x:
        if i > z:
            z = i
    print(z)

def min_while_loop(x):
    z = x[0]
    for i in x:
        while i < z:
            z = i
    print(z)

def max_while_loop(x):
    z = x[0]
    for i in x:
        while i > z:
            z = i
    print(z)