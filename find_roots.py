from math import sqrt

def find_roots(a, b, c):
    r = ( ((-b + sqrt(b**2 - (4*a*c))) / (2*a)), ((-b - sqrt(b**2 - (4*a*c))) / (2*a)) )
    return r

print(find_roots(2, 10, 8))