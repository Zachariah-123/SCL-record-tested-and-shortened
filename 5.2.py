'''5.2 AIM: Integrate the below function using the general
integration tool such as quad in the interval [-2,2]
f(t) = 4t2 + 3'''
import numpy as np
from scipy.integrate import quad
import time
def f(t):
    return 4*t**2+3
result,error = quad(f,-2,2)
print(f'''Result={result}
Error={error}''')
