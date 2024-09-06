import sympy as sp

def maclaurin_series(f, x, N):
    """
    Calcula la aproximación de Maclaurin (serie de Taylor en a=0) de la función f(x) hasta el orden N.
    
    :param f: Función a aproximar
    :param x: Variable independiente
    :param N: Orden de la aproximación de Maclaurin
    :return: Expresión de la serie de Maclaurin
    """
    maclaurin_approx = 0
    terms = []
    for n in range(N + 1):
        term = (f.diff(x, n).subs(x, 0) / sp.factorial(n)) * (x)**n
        maclaurin_approx += term
        terms.append(term)
    
    return maclaurin_approx, terms

# Definición de los datos
x = sp.symbols('x')
f = x**2 + 3*x  # Ejemplo: función cuadrática

N = 2  # Orden de la aproximación
x_value = 1.5  # Valor específico de x
tolerancia = 0.01  # Tolerancia aceptable del error

# Cálculo de la serie de Maclaurin y obtención de términos individuales
maclaurin_approx, terms = maclaurin_series(f, x, N)

# Mostrar el término x_0 (orden 0) y x_1 (orden 1)
x_0 = terms[0]  # Término constante
x_1 = terms[1]  # Término lineal

# Evaluación de la serie en x_value
maclaurin_evaluated = maclaurin_approx.subs(x, x_value)

# Valor exacto de la función
valor_exacto = f.subs(x, x_value)

# Cálculo del error absoluto
error = abs(valor_exacto - maclaurin_evaluated)

# Mostrar los resultados intermedios para depuración
print(f"Término x_0 (constante): {x_0}")
print(f"Término x_1 (lineal): {x_1}")

print(f"\nSerie de Maclaurin de {f} hasta el orden {N}:")
print(maclaurin_approx)

print(f"\nEvaluación de la serie de Maclaurin en x = {x_value}:")
print(maclaurin_evaluated)

print(f"\nValor exacto de la función en x = {x_value}:")
print(valor_exacto)

print(f"\nError: {error}")

# Comparación con la tolerancia
if error < tolerancia:
    mensaje = f"El error {error} está dentro de la tolerancia ({tolerancia})."
else:
    mensaje = f"El error {error} excede la tolerancia ({tolerancia})."

print(mensaje)
