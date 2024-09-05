import math

# Definir las variables
B = 20  # Ancho en metros
H = 0.3  # Profundidad en metros
n = 0.03  # Coeficiente de rugosidad
S = 0.0003  # Pendiente

# Calcular el flujo nominal Q usando la fórmula de Manning
def calcular_flujo(B, H, n, S):
    return (1 / n) * B * H * ((B + 2 * H) / B) ** (2 / 3) * S ** 0.5

Q = calcular_flujo(B, H, n, S)

# Derivadas parciales
def derivada_parcial_n(Q, n):
    return -Q / n

def derivada_parcial_S(Q, S):
    return 0.5 * Q / S

# Variaciones
delta_n = 0.1 * n  # ±10% de n
delta_S = 0.1 * S  # ±10% de S

# Sensibilidad
sensibilidad_n = abs(derivada_parcial_n(Q, n)) * delta_n
sensibilidad_S = abs(derivada_parcial_S(Q, S)) * delta_S

# Imprimir resultados
print(f"Flujo nominal Q: {Q:.4f} m³/s")
print(f"Derivada parcial de Q con respecto a n: {derivada_parcial_n(Q, n):.4f}")
print(f"Derivada parcial de Q con respecto a S: {derivada_parcial_S(Q, S):.4f}")
print(f"Cambio en Q debido a variación en n (±10%): {sensibilidad_n:.4f} m³/s")
print(f"Cambio en Q debido a variación en S (±10%): {sensibilidad_S:.4f} m³/s")
