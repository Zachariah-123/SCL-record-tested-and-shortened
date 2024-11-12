'''3.2.2 AIM: Program to find the solution of linear equation using python
 a) 3x + y + 6z = 10
 b) 4x + 3y-3z =-5
 c) 6x + 7y + 9z =20'''


import numpy as np
mat = [[3,1,6] ,[4,3,-3], [6,7,9] ]
solmat =[10 ,-5, 20]
inverse = np.linalg.inv(mat)
prod = inverse@solmat
for i in range (np.linalg.matrix_rank(inverse)):
    print(prod[i])
