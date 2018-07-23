def gcd(x,b):
    while b > 0:
        x, b = b, x % b
    return x
def lcm(x, b):
    return x * b / gcd(x, b)
x,b=map(int,input("Enter the values:").split(' '))
print(int(lcm(x,b)))
