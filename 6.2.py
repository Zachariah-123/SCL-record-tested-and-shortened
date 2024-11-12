'''6.2 AIM : Realize the function sinx = x−x
3/3! +x
5/5!−. . . ..
for the first 5 and 20 terms and understand the convergence'''

import numpy as np
from math import factorial

def sine(x,n):
    even_term,odd_term=0,0
    for i in range(1,(n+1),4):
        even_term +=pow(x,i)/(factorial(i))
    for i in range(3,(n+1),4):              
        odd_term += pow(x,i)/(factorial(i))
    return (even_term - odd_term)

print(sine(3,1))
print(sine(3,100))
