import math

# Definir la función original f(x) = ln(x)
def f(x):
    return math.log(x)

# Derivadas de la función f(x) = ln(x)
def f_prime(x):
    return 1 / x

def f_double_prime(x):
    return -1 / x**2

def f_triple_prime(x):
    return 2 / x**3

def f_quadruple_prime(x):
    return -6 / x**4

# Expansión de Taylor hasta el cuarto orden en torno a x0
def taylor_approximation(x, x0, order):
    result = f(x0)  # Orden 0 (constante)
    
    if order >= 1:
        result += f_prime(x0) * (x - x0)  # Orden 1 (lineal)
        
    if order >= 2:
        result += (f_double_prime(x0) * (x - x0)**2) / math.factorial(2)  # Orden 2 (cuadrático)
        
    if order >= 3:
        result += (f_triple_prime(x0) * (x - x0)**3) / math.factorial(3)  # Orden 3 (cúbico)
        
    if order >= 4:
        result += (f_quadruple_prime(x0) * (x - x0)**4) / math.factorial(4)  # Orden 4 (cuártica)
        
    return result

# Calcular el error relativo porcentual
def relative_error(true_value, approx_value):
    return abs((true_value - approx_value) / true_value) * 100

# Solicitar entrada de x0 y x_target al usuario
x0 = float(input("Ingrese el valor de x0 (punto base): "))
x_target = float(input("Ingrese el valor de x_target (punto donde se evaluará la función): "))

# Valor verdadero de f(x) en x = x_target
true_value = f(x_target)

# Calcular las aproximaciones y los errores para órdenes 0 a 4
for order in range(5):
    approx_value = taylor_approximation(x_target, x0, order)
    error = relative_error(true_value, approx_value)
    
    print(f"\nAproximación de orden {order}: {approx_value:.5f}")
    print(f"Error relativo porcentual: {error:.2f}%")

# Mostrar el valor verdadero
print(f"\nValor verdadero f({x_target}) = {true_value:.5f}")
