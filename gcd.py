def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)
    
print(gcd(4,2))    