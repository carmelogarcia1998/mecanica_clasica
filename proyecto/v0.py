import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del sistema
m = 1   # Masa del péndulo
l = 1.0  # Longitud del péndulo
k = 1 # Constante del resorte
h = l / 2  # Longitud natural del resorte cuando no está comprimido o extendido
Q0 = 2.0  # Amplitud de la fuerza externa
Omega = 1.0  # Frecuencia de la fuerza externa
g = 9.81  # Aceleración debida a la gravedad
B = 0.5  # Amortiguación

# Definir las ecuaciones del movimiento
def equations(z, t):
    theta, dthetadt = z
    d2thetadt2 = ((Q0 / (m * l)) * np.cos(Omega * t) * np.cos(theta) + (g / l) * np.sin(theta) - (B / (m * l**2)) * dthetadt - ((k * h**2) / (m * l**2)) * np.sin(theta) * np.cos(theta))
    return [dthetadt, d2thetadt2]

# Condiciones iniciales
initial_conditions = [
    [np.pi / 4, 0.0],  # Caso 1: Ángulo inicial de π/4 radianes, velocidad angular inicial 0
    [np.pi / 6, 0.0],  # Caso 2: Ángulo inicial de π/6 radianes, velocidad angular inicial 0
    [np.pi / 3, 0.0],  # Caso 3: Ángulo inicial de π/3 radianes, velocidad angular inicial 0
    [np.pi / 2, 0.0]   # Caso 4: Ángulo inicial de π/2 radianes, velocidad angular inicial 0
]

# Intervalo de tiempo para la simulación
t = np.linspace(0, 100, 5000)

# Graficar las órbitas
plt.figure(figsize=(10, 8))

for z0 in initial_conditions:
    # Resolver el sistema de ecuaciones diferenciales
    sol = odeint(equations, z0, t)
    
    # Extraer las soluciones
    theta_sol = sol[:, 0]
    dthetadt_sol = sol[:, 1]
    
    # Graficar el espacio de fases (θ, dθ/dt)
    plt.plot(theta_sol, dthetadt_sol, label=f'θ0={z0[0]}, dθ/dt0={z0[1]}')

# Graficar la línea de velocidad cero
theta_range = np.linspace(0, np.pi / 2, 500)
zero_velocity = np.zeros_like(theta_range)
plt.plot(theta_range, zero_velocity, 'k--', label='Velocidad cero')

plt.xlabel('Ángulo (θ)')
plt.ylabel('Velocidad angular (dθ/dt)')
plt.title('Órbitas del Sistema en el Espacio de Fases')
plt.legend()
plt.grid(True)
plt.show()
