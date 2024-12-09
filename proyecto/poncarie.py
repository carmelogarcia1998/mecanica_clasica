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
# Condiciones iniciales
theta0 = np.pi / 4  # Ángulo inicial (en radianes)
dthetadt0 = 0.0  # Velocidad angular inicial
z0 = [theta0, dthetadt0]

# Intervalo de tiempo para la simulación
t = np.linspace(0, 200, 10000)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(equations, z0, t)

# Extraer las soluciones
theta_sol = sol[:, 0]
dthetadt_sol = sol[:, 1]

# Generar el diagrama de Poincaré
poincare_theta = []
poincare_dtheta = []
interval = int(len(t) / (20 * np.pi / Omega))  # Intervalo de muestreo basado en el período de la fuerza externa

for i in range(0, len(t), interval):
    poincare_theta.append(theta_sol[i])
    poincare_dtheta.append(dthetadt_sol[i])

# Graficar el diagrama de Poincaré
plt.figure(figsize=(8, 6))
plt.scatter(poincare_theta, poincare_dtheta, s=1, color='blue')
plt.xlabel('Ángulo (theta)')
plt.ylabel('Velocidad angular (dtheta/dt)')
plt.title('Diagrama de Poincaré')
plt.grid(True)
plt.show()
