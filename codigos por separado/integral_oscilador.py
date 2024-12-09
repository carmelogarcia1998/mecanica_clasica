import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



L, w, A, m = 1, 2.5, 0.1, 1
# The gravitational acceleration (m.s-2).
g = 9.81

def deriv(y, t, L, w, A, m):
    """Calcula la primera derivada tras la redución del ordem"""
    theta, thetadot = y
    dtheta_dt = thetadot
    dthetadot_dt = (A * w**2 / L * np.cos(w*t) * np.cos(theta) -
                   g * np.sin(theta))
    return dtheta_dt, dthetadot_dt

# Se integra hasta 40 grados en 0.01 grados
tmax, dt = 40, 0.01
t = np.arange(0, tmax+dt, dt)
# Condicion inicial para theta, dtheta/dt
y0 = [0, 0]

# Integro la ec. de movimiento
y = odeint(deriv, y0, t, args=(L, w, A, m))
# La solución indica tanto el valor del ángulo como el de la derivada del mismo
theta, thetadot = y[:,0], y[:,1]

plt.plot(t,theta)
plt.show()

