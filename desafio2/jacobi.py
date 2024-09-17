import numpy as np

# Función para ingresar la matriz A y el vector b del sistema de ecuaciones
def ingresar_datos():
    # Ingresar el número de ecuaciones (filas y columnas)
    n = int(input("Ingrese el número de ecuaciones: "))
    
    A = np.zeros((n, n))  # Matriz de coeficientes A
    b = np.zeros(n)       # Vector de términos independientes b
    
    # Ingresar los coeficientes de la matriz A
    print("Ingrese los coeficientes de la matriz (una fila a la vez):")
    for i in range(n):
        A[i] = [float(x) for x in input(f"Fila {i+1}: ").split()]
    
    # Ingresar el vector de términos independientes b
    print("Ingrese el vector de términos independientes (una fila):")
    b = [float(x) for x in input("Vector b: ").split()]
    
    return A, np.array(b)

# Método de Jacobi
def jacobi(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros(n)  # Inicialización de la solución
    
    D = np.diag(np.diag(A))  # Matriz diagonal
    R = A - D                # Matriz residual (A sin la diagonal)

    for i in range(max_iterations):
        x_new = (b - np.dot(R, x)) / np.diag(A)  # Actualización de Jacobi

        # Chequeamos si la diferencia entre las iteraciones es menor a la tolerancia
        if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
            return x_new, i  # Solución encontrada y número de iteraciones

        x = x_new  # Actualizamos el valor de x

    return x, max_iterations  # Si no converge, devolvemos el valor obtenido

# Función principal
def main():
    A, b = ingresar_datos()  # Ingresamos los datos del sistema de ecuaciones

    # Aplicamos el método de Jacobi
    solution, iterations = jacobi(A, b)

    # Mostramos los resultados
    print("\nSolución encontrada:")
    for i in range(len(solution)):
        print(f"x{i+1} = {solution[i]:.5f}")
    
    print(f"Iteraciones: {iterations}")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
