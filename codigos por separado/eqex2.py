import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Parámetros del sistema
m = 1   # Masa del péndulo
l = 1.0  # Longitud del péndulo
k = 1  # Constante del resorte
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
theta0 = np.pi / 3  # ángulo inicial (en radianes)
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
pendulum_x = l * np.cos(theta_sol)
pendulum_y = l * np.sin(theta_sol)

# Coordenadas del resorte
spring_x = h * np.cos(theta_sol) 
spring_y = h * np.sin(theta_sol)

# Crear la figura y el eje para la animación
fig, ax = plt.subplots()
ax.set_xlim(-l - 0.5, l + 0.5)
ax.set_ylim(-l - 0.5, l + 0.5)
ax.axvline(-B, color='gray', linestyle='--')
line_pendulum, = ax.plot([], [], 'o-', lw=2, color='blue')
line_spring, = ax.plot([], [], color='red', linestyle='-', lw=1)

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
    line_spring.set_data([-B, spring_x[frame]], [h, spring_y[frame]])
    
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
plt.plot(t, dthetadt_sol, label='Velocidad angular (dtheta/dt)', color='r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad angular (rad/s)')
plt.legend()

plt.tight_layout()
plt.show()
