from scipy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def vdp(t, z):
    x, y = z
    return [y, mu*(1 - x**2)*y - x]



mus = [0, 1, 2]
styles = ["-", "--", ":"]

a, b = 0, 10
t = linspace(a, b, 500)

for mu in mus:
      sol = solve_ivp(vdp, [a, b], [1, 0], t_eval=t)
      plt.plot(sol.t, sol.y[0], styles[mu],label=mus[mu])
      
      
      
      

plt.legend()
plt.show()

