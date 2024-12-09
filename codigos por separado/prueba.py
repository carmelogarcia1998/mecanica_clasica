import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Parámetros del sistema
m = 1.0   # Masa del péndulo
l0 = 1.0  # Longitud natural del resorte
k = 40 # Constante del resorte
g = 9.81  # Aceleración debida a la gravedad

# Definir las ecuaciones del movimiento
def equations(y, t, m, l0, k, g):
    l, ld, theta, thetad = y
    ldd = (m * l * thetad**2 - k * (l - l0) + m * g * np.cos(theta)) / m
    thetadd = (-2 * ld * thetad - g * np.sin(theta)) / l
    return [ld, ldd, thetad, thetadd]

# Condiciones iniciales
l0 = 1.0
l_init = l0 + 0.2  # Longitud inicial del resorte ligeramente extendida
ld_init = 0.0  # Velocidad inicial del resorte
theta_init = np.pi / 4  # Ángulo inicial del péndulo
thetad_init = 0.0  # Velocidad angular inicial
y0 = [l_init, ld_init, theta_init, thetad_init]

# Intervalo de tiempo
t = np.linspace(0, 20, 1000)

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(equations, y0, t, args=(m, l0, k, g))

# Extraer las soluciones
l_sol = sol[:, 0]
ld_sol = sol[:, 1]
theta_sol = sol[:, 2]
thetad_sol = sol[:, 3]

# Convertir las posiciones angulares a coordenadas x, y del péndulo
pendulum_x = l_sol * np.sin(theta_sol)
pendulum_y = -l_sol * np.cos(theta_sol)

# Crear la figura y el eje para la animación
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line_pendulum, = ax.plot([], [], 'o-', lw=2, color='blue')
line_spring, = ax.plot([], [], color='red', linestyle='-', lw=2)

# Función de inicialización
def init():
    line_pendulum.set_data([], [])
    line_spring.set_data([], [])
    return line_pendulum, line_spring

# Función de animación
def update(frame):
    # Actualizar datos del péndulo
    line_pendulum.set_data([0, pendulum_x[frame]], [0, pendulum_y[frame]])
    
    # Actualizar datos del resorte
    line_spring.set_data([0, pendulum_x[frame]], [0, pendulum_y[frame]])
    
    return line_pendulum, line_spring

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
plt.plot(t, ld_sol, label='Velocidad del resorte (ld)', color='r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()

plt.tight_layout()
plt.show()
