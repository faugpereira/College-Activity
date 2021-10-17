import numpy as np

A = np.array([[4, 3, 2], [6, 4, 5], [2, 2, 1]])
print('\nA = \n',A)
B = np.array([[42.50], [68.50], [23.50]])
print('\nB = \n', B)

detA = np.linalg.det(A)
print('\nDeterminante de A = \n', detA)

inversaA = np.linalg.inv(A)
print('\nA inversa de A = \n', inversaA)

x = inversaA @ B
print('\nX = \n', x)