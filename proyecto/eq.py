import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
'''
# Definir las ecuaciones del movimiento
def equations(z, t, m=1.0, l=1.0, k=0.5, Q0=1.0, Omega=1.0, g=9.81):
    x, dxdt, theta, dthetadt = z
    # Ecuaciones de movimiento
    d2xdt2 = (m * l * (theta * (-(dxdt * dthetadt + np.cos(theta))) + (dthetadt ** 2)) + k * x + Q0 * np.cos(Omega * t)) / m
    d2thetadt2 = (-(dxdt * dthetadt) - ((d2xdt2 - dxdt) * theta) - (dthetadt * l)) / l
    return [dxdt, d2xdt2, dthetadt, d2thetadt2] '''

# Definir las ecuaciones del movimiento
def equations(z, t, m=1.0, l=1.0, k=0.5, Q0=1.0, Omega=1.0, g=9.81, V=1):
    x, dxdt, theta, dthetadt = z
    # Ecuaciones de movimiento
    d2xdt2 = V - k/m * x - Q0/m * np.cos(Omega * t)
    d2thetadt2 = V/(theta * l) - (dthetadt)**2 /theta
    return [dxdt, d2xdt2, dthetadt, d2thetadt2]

# Condiciones iniciales
x0 = 0.0       # posición inicial
dxdt0 = 0.0    # velocidad inicial
theta0 = np.pi / 2  # ángulo inicial (en radianes)
dthetadt0 = 0.0     # velocidad angular inicial
z0 = [x0, dxdt0, theta0, dthetadt0]

# Intervalo de tiempo
t = np.linspace(0, 10, 1000)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(equations, z0, t)

# Extraer las soluciones
x_sol = sol[:, 0]
dxdt_sol = sol[:, 1]
theta_sol = sol[:, 2]
dthetadt_sol = sol[:, 3]

# Graficar los resultados
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x_sol, label='Posición (x)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Solución de las ecuaciones de movimiento')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, dxdt_sol, label='Velocidad (dx/dt)', color='r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, theta_sol, label='Ángulo (theta)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.legend()

plt.tight_layout()
plt.show()
