#3.1.3 AIM Program to find the angle between two vectors

import numpy as np
import math
def inputvec(n,v):
    for i in range (n):
        ele = eval(input(f"Enter the element {i+1} :"))
        v.append(ele)
    return np.array(v)

def dp( n , v , v1):
    mag = 0
    for i in range (n):
        mag += v[i]*v1[i]
    return mag

def mag(n,v):
    s = 0
    for i in range (n):
        s += v[i]**2
    return s**0.5
terms = int ( input ("Enter number of terms :") ) 
vec , vec1 = [] , []
vec = inputvec(terms  , vec)
vec1 = inputvec(terms , vec1)
dotprod = dp (terms , vec , vec1)
magvec = mag (terms , vec)
magvec1 = mag(terms , vec1)
print(f'angle = {math.degrees(math.acos(dotprod/(magvec * magvec1)))  }')
