import math

# Definir la función original f(x)
def f(x):
    return 25*x**3 - 6*x**2 + 7*x - 88

# Derivadas de la función f(x)
def f_prime(x):
    return 75*x**2 - 12*x + 7

def f_double_prime(x):
    return 150*x - 12

def f_triple_prime(x):
    return 150

# Expansión de Taylor hasta el tercer orden en torno a x0
def taylor_approximation(x, x0, order):
    result = f(x0)  # Orden 0 (constante)
    
    if order >= 1:
        result += f_prime(x0) * (x - x0)  # Orden 1 (lineal)
        
    if order >= 2:
        result += (f_double_prime(x0) * (x - x0)**2) / math.factorial(2)  # Orden 2 (cuadrático)
        
    if order >= 3:
        result += (f_triple_prime(x0) * (x - x0)**3) / math.factorial(3)  # Orden 3 (cúbico)
        
    return result

# Calcular el error relativo porcentual
def relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Solicitar entrada de x0 y x_target al usuario
x0 = float(input("Ingrese el valor de x0 (punto base): "))
x_target = float(input("Ingrese el valor de x_target (punto donde se evaluará la función): "))

# Valor verdadero de f(x) en x = x_target
true_value = f(x_target)

# Calcular las aproximaciones y los errores para órdenes 0 a 3
for order in range(4):
    approx_value = taylor_approximation(x_target, x0, order)
    error = relative_error(true_value, approx_value)
    
    print(f"\nAproximación de orden {order}: {approx_value:.4f}")
    print(f"Error relativo porcentual: {error:.4f}%")

# Mostrar el valor verdadero
print(f"\nValor verdadero f({x_target}) = {true_value:.4f}")
