import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del sistema
m = 1   # Masa del péndulo
l = 1.0  # Longitud del péndulo
k = 10000  # Constante del resorte
h = 0.7*l  # Longitud natural del resorte cuando no está comprimido o extendido
Q0 = 1.0  # Amplitud de la fuerza externa
Omega = 1.0  # Frecuencia de la fuerza externa
g = 9.81  # Aceleración debida a la gravedad
B = 0   # Distancia la base del pendulo al origen

# Definir las ecuaciones del movimiento
def equations(z, t):
    theta, dthetadt = z
    d2thetadt2 =  (Q0/m*l**2)*np.cos(Omega*t) + (g/l - ((k*h**2)/(m*l**2))*np.cos(theta))*np.sin(theta) - ((B*k*h)/(m*l**2))*np.cos(theta)
    return [dthetadt, d2thetadt2]

# Parámetros para el cálculo del exponente de Lyapunov
dt = 0.01
Tmax = 200
n_steps = int(Tmax / dt)
epsilon = 1e-8  # Perturbación inicial

# Inicializar las condiciones iniciales y las trayectorias
z0 = [np.pi / 4, 0.0]
z0_perturbed = [np.pi / 4 + epsilon, 0.0]

# Función para integrar y obtener trayectorias
def integrate(z0, dt, n_steps):
    trajectory = np.zeros((n_steps, 2))
    z = z0
    for i in range(n_steps):
        trajectory[i] = z
        z = odeint(equations, z, [0, dt])[1]
    return trajectory

trajectory = integrate(z0, dt, n_steps)
trajectory_perturbed = integrate(z0_perturbed, dt, n_steps)

# Cálculo del exponente de Lyapunov
lyapunov_exp = np.zeros(n_steps)
for i in range(n_steps):
    delta_z = trajectory_perturbed[i] - trajectory[i]
    delta_norm = np.linalg.norm(delta_z)
    if delta_norm == 0:
        delta_norm = epsilon  # Evitar división por cero
    lyapunov_exp[i] = np.log(delta_norm / epsilon)

lyapunov_exp = np.cumsum(lyapunov_exp) / np.arange(1, n_steps + 1)

# Graficar el exponente de Lyapunov
plt.figure(figsize=(10, 6))
plt.plot(np.arange(n_steps) * dt, lyapunov_exp, label='Exponente de Lyapunov')
plt.xlabel('Tiempo')
plt.ylabel('Exponente de Lyapunov')
plt.title('Cálculo del Exponente de Lyapunov para el Sistema')
plt.legend()
plt.grid(True)
plt.show()
