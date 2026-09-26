import numpy as np

A = np.array([
    [2, -4], 
    [-6, 8]])
B = np.array([
    [1, -3], 
    [-5, -7]])

print("Sum:", A+B)
print("Difference:", A-B)
print("Dot product:", np.dot(A, B))
print("Transpose of A:", A.T)
print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:", np.linalg.inv(A))