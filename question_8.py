#Question 8: Digital Root
def digital_root(x):
    z = 0
    n =  str(x)
    q = len(n)-1
    r = 0
    while q > -1:
        p = (x // 10**q) - r*10
        r = (x//10**q)
        q -= 1
        z += p
    print(z)
