import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos el sistema de ecuaciones
# 10x + 2y - z = 27
# -3x - 6y + 2z = -61.5
# x + y + 5z = -21.5

# Definimos las matrices del sistema
A = np.array([[10, 2, -1],
              [-3, -6, 2],
              [1, 1, 5]])
b = np.array([27, -61.5, -21.5])

# Resolvemos el sistema de ecuaciones
intersection_point = np.linalg.solve(A, b)

# Funciones para cada plano
def plane1(x, y):
    return 10*x + 2*y - 27

def plane2(x, y):
    return (-3*x - 6*y + 61.5) / 2

def plane3(x, y):
    return (-x - y - 21.5) / 5

# Creamos una malla de puntos
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Calculamos Z para cada plano
Z1 = plane1(X, Y)
Z2 = plane2(X, Y)
Z3 = plane3(X, Y)

# Configuración de la gráfica
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficamos cada plano
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='r', label='10x + 2y - z = 27')
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='g', label='-3x - 6y + 2z = -61.5')
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='b', label='x + y + 5z = -21.5')

# Etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfica 3D de los planos del sistema de ecuaciones')

# Agregar leyenda manualmente
ax.text(x=0, y=0, z=27, s='10x + 2y - z = 27', color='r')
ax.text(x=0, y=0, z=-61.5, s='-3x - 6y + 2z = -61.5', color='g')
ax.text(x=0, y=0, z=-21.5, s='x + y + 5z = -21.5', color='b')

# Mostrar el punto de intersección
ax.scatter(*intersection_point, color='k', s=100, label='Intersección')
ax.text(intersection_point[0], intersection_point[1], intersection_point[2],
        f'Intersección\n{intersection_point}', color='k', fontsize=12)

# Mostrar la gráfica
plt.show()
