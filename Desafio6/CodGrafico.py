import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear una cuadrícula de valores para x y y
x = np.linspace(-10, 20, 100)
y = np.linspace(-40, 10, 100)
X, Y = np.meshgrid(x, y)

# Definir las ecuaciones del sistema
# Z1 = (9 - 2x - y)
Z1 = (9 - 2*X - Y)
# Z2 = (21 - 3x - 2y)/3
Z2 = (21 - 3*X - 2*Y)/3
# Z3 = (23 - x - 4y)/9
Z3 = (23 - X - 4*Y)/9

# Graficar los planos de cada ecuación
ax.plot_surface(X, Y, Z1, color='red', alpha=0.6, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z2, color='green', alpha=0.6, rstride=100, cstride=100)
ax.plot_surface(X, Y, Z3, color='blue', alpha=0.6, rstride=100, cstride=100)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título del gráfico
ax.set_title('Sistema de ecuaciones lineales en 3D')

# Mostrar la gráfica
plt.show()
