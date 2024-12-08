import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1   # Masa del péndulo
l = 1.0  # Longitud del péndulo
k = 1000  # Constante del resorte
h = l / 2  # Longitud natural del resorte cuando no está comprimido o extendido
Q0 = 1.0  # Amplitud de la fuerza externa
Omega = 1.0  # Frecuencia de la fuerza externa
g = 9.81  # Aceleración debida a la gravedad
B = 0.5   # Amortiguación

# Definir la función de equilibrio
def equilibrium(theta):
    return (Q0 * np.cos(Omega * 0) * np.cos(theta) + g * np.sin(theta) - (k * h**2 / (m * l)) * np.sin(theta) * np.cos(theta)) / (m * l)

# Encontrar los puntos de equilibrio usando fsolve
theta_initial_guesses = np.linspace(0, np.pi / 2, 100)
equilibrium_points = fsolve(equilibrium, theta_initial_guesses)

# Filtrar valores duplicados y mantener solo los puntos de equilibrio únicos
unique_equilibrium_points = np.unique(np.round(equilibrium_points, decimals=5))

# Mostrar los puntos de equilibrio
print("Puntos de equilibrio (Lagrange):", unique_equilibrium_points)

# Graficar la función de equilibrio
theta_vals = np.linspace(0, np.pi / 2, 400)
equilibrium_vals = equilibrium(theta_vals)

plt.plot(theta_vals, equilibrium_vals, label='Función de equilibrio')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(unique_equilibrium_points, equilibrium(unique_equilibrium_points), color='red', zorder=5)
plt.xlabel('Ángulo (theta)')
plt.ylabel('Función de equilibrio')
plt.title('Puntos de equilibrio del sistema')
plt.legend()
plt.grid(True)
plt.show()