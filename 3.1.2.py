# 3.1.2 AIM: Program to add N Vectors
import numpy as np
def inputvec(n,v):
    for i in range (n):
        ele = int(input(f"Enter the element {i+1} :"))
        v.append(ele)
    return np.array(v)
terms = int(input("Enter number of elements:"))
v1 ,v2 =[] , []
v1 = inputvec(terms , v1)
v2 = inputvec(terms , v2)
print(v1,v2)
