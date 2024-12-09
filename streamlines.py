import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline
from scipy.optimize import fsolve

# Parámetros del sistema
m = 1   # Masa del péndulo
l = 1.0  # Longitud del péndulo
k = 1  # Constante del resorte
h = 0.7*l  # Longitud natural del resorte cuando no está comprimido o extendido
Q0 = 1.0  # Amplitud de la fuerza externa
Omega = 1.0  # Frecuencia de la fuerza externa
g = 9.81  # Aceleración debida a la gravedad
B = 0   # Distancia la base del pendulo al origen

# Definir la función de equilibrio
def equilibrium(theta):
    return ((Q0/m*l**2)*np.cos(Omega*0) + (g/l - ((k*h**2)/(m*l**2))*np.cos(theta))*np.sin(theta) - ((B*k*h)/(m*l**2))*np.cos(theta))

# Encontrar los puntos de equilibrio usando fsolve
theta_initial_guesses = np.linspace(0, np.pi / 2, 100)
equilibrium_points = fsolve(equilibrium, theta_initial_guesses)

# Filtrar valores duplicados y mantener solo los puntos de equilibrio únicos
unique_equilibrium_points = np.unique(np.round(equilibrium_points, decimals=5))

# Mostrar los puntos de equilibrio
print("Puntos de equilibrio (Lagrange):", unique_equilibrium_points)

# Graficar la función de equilibrio
theta_vals = np.linspace(0, np.pi, 400)
equilibrium_vals = equilibrium(theta_vals)

#plt.plot(theta_vals, equilibrium_vals, label='Función de equilibrio')
plt.axhline(0, color='gray', linestyle='--')
plt.scatter(unique_equilibrium_points, equilibrium(unique_equilibrium_points), color='red', zorder=5)

# range of x and y grid
xmax = np.pi*6.5
ymax = 6
fac=1.01
# hacer una cuadrícula de valores x e y, Y =  X punto
X,Y = np.meshgrid(np.arange(-xmax,xmax,.1),np.arange(-ymax,ymax,.1) )
epsilon=0.4
H = 0.5*Y*Y/(m*l**2)  + m*g*l*np.cos(X) + 0.5*k*(np.sin(X)*h +B )*(np.sin(X)*h +B) #Este es el hamiltoniano
# Las ecuaciones de Hamilton nos dan un campo vectorial U,V
U = Y/(m*l**2 ) # dH/dp
V = m*g*l*np.sin(X) - k*h*(h*np.sin(X) + B)*np.cos(X)  # dH/dtheta

fig, ax = plt.subplots(1,1,figsize=(4,4))
ax.set_title('Puntos de Lagrange')
ax.set_xlabel(r'$ \theta$')
ax.set_ylabel(r'd$\theta$/dt')
ax.set_xlim([-xmax*fac, xmax*fac])
ax.set_ylim([-ymax*fac, ymax*fac])
#plt.plot(theta_vals, equilibrium_vals, label='Función de equilibrio')
#plt.axhline(0, color='gray', linestyle='--')
ax.scatter(unique_equilibrium_points, equilibrium(unique_equilibrium_points), color='red', zorder=5)

# guardar la imagen .jpg
plt.savefig('lagrange.jpg')

# plot the vector field here with either of the two commands below
#Q = plt.quiver(X,Y,U, V)
Q = ax.streamplot(X,Y,U, V,density=2)
plt.show()