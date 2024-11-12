'''3.2.3 AIM: Program to read a square matrix and verify
 Eigen value decomposition theorem'''
import numpy as np

def matrixinput(n):
    A=np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            A[i][j]= int(input(f"Enter the element number {i},{j}:"))
    print(A)
    return A
term = int(input("Enter the rank of the matrix:"))
A = matrixinput(term)
eigval , eigvec = np.linalg.eig(A)
diag = np.diag(eigval)
inv = np.linalg.inv(eigvec)
print(eigvec@diag@inv)
