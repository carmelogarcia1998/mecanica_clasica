import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Parámetros del sistema
m = 1   # Masa del péndulo
l = 1.0    # Longitud del péndulo
k = 1000    # Constante
h = l/2  # Constante adicional
Q0 = 1.0   # Amplitud de la fuerza externa
Omega = 1.0 # Frecuencia de la fuerza externa
g = 9.81   # Aceleración debida a la gravedads
B = 0.5

# Definir las ecuaciones del movimiento
def equations(z, t):
    theta, dthetadt = z
    d2thetadt2 = ((Q0/ m*l) * np.cos(Omega * t) * np.cos(theta) + g/l * np.sin(theta)) - (B/(m*l**2)) * dthetadt - ((k*h**2) /m*l**2) * np.sin(theta)*np.cos(theta)
    return [dthetadt, d2thetadt2]



# Condiciones iniciales
theta0 = np.pi / 3 # ángulo inicial (en radianes)
dthetadt0 = 0.0     # velocidad angular inicial
z0 = [theta0, dthetadt0]

# Intervalo de tiempo
t = np.linspace(0, 10, 1000)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(equations, z0, t)

# Extraer las soluciones
theta_sol = sol[:, 0]
dthetadt_sol = sol[:, 1]

# Convertir las posiciones angulares a coordenadas x, y del péndulo
# Convertir las posiciones angulares a coordenadas x, y del péndulo
pendulum_x = l * np.cos(theta_sol) 
pendulum_y = l * np.sin(theta_sol)

# Crear la figura y el eje para la animación
fig, ax = plt.subplots()
ax.set_xlim(-l-0.5, l+0.5)
ax.set_ylim(-l-0.5, l+0.5)
ax.axvline(-0.5, color='gray', linestyle='--') 
line, = ax.plot([], [], 'o-', lw=2)

# Función de inicialización
def init():
    line.set_data([], [])
    return line,

# Función de animación
def update(frame):
    line.set_data([0, pendulum_x[frame]], [0, pendulum_y[frame]])
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=range(len(t)), init_func=init, blit=True)

# Mostrar la animación
plt.show()

# Graficar los resultados
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, theta_sol, label='Ángulo (theta)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.title('Solución de la ecuación de movimiento')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, dthetadt_sol, label='Velocidad angular (dtheta/dt)', color='r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad angular (rad/s)')
plt.legend()

plt.tight_layout()
plt.show()
