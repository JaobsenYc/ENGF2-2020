def gcd(a,b):
    while not a==b:
        if a%2!=0 and b%2!=0:
            a=a/2
            b=b/2
        if a>b:
            a=a-b
        else:
            b=b-a
    return  a

ax=48
bx=72
print(f"GCD of {ax} and {bx} is {gcd(ax,bx)}")
