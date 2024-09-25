import numpy as np

# Definir la matriz de coeficientes A y el vector de términos independientes B
A = np.array([[2, 1, 1], [3, 2, 3], [1, 4, 9]])
B = np.array([9, 21, 23])

# Resolver el sistema de ecuaciones (X = A^-1 * B)
X = np.linalg.solve(A, B)

# Calcular el determinante de A
determinante = np.linalg.det(A)

# Calcular la matriz condicional
condicional = np.linalg.cond(A)

# Imprimir resultados
print("Solución del sistema de ecuaciones: x =", X[0], ", y =", X[1], ", z =", X[2])
print("Determinante de la matriz A:", determinante)
print("Número condicional de la matriz A:", condicional)
