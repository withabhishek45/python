def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(12, 18))  
